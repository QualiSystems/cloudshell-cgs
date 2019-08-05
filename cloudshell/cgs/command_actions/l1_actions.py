import re
from collections import defaultdict
from dataclasses import dataclass
from typing import TYPE_CHECKING, Iterable, Iterator, List, Mapping

from cloudshell.cgs.cli.command_modes import ConfigCommandMode, EnableCommandMode
from cloudshell.cgs.command_actions.base_actions import BaseCgsActions
from cloudshell.cgs.command_templates.configuration_commands import COMMIT
from cloudshell.cgs.command_templates.l1_commands import (
    CONNECT_PORTS,
    DELETE_FILTERS,
    SHOW_CONNECTIONS,
)
from cloudshell.cgs.helpers.errors import (
    ParseFilterError,
    UnsupportedPortsInFilterError,
)
from cloudshell.cgs.helpers.table2dicts import ParseTableError, table2dicts

if TYPE_CHECKING:
    from logging import Logger


@dataclass(frozen=True)
class Filter:
    ADMIN_ENABLED = "enabled"
    ACTION_REDIRECT = "redirect"
    PORT_PATTERN = re.compile(r"^\d+(/\d+)?$")

    id: str
    admin: str
    action: str
    input_port: str
    output_port: str

    def __post_init__(self):
        self.validate()

    @classmethod
    def from_dict(cls, dict_: Mapping) -> "Filter":
        return cls(
            dict_["Filter"],
            dict_["Admin"],
            dict_["Action"],
            dict_["Input"],
            dict_["Output"],
        )

    @property
    def is_enabled(self) -> bool:
        return self.admin.lower() == self.ADMIN_ENABLED

    @property
    def is_redirect(self) -> bool:
        return self.action.lower() == self.ACTION_REDIRECT

    def validate(self) -> None:
        self.validate_port(self.input_port)
        self.validate_port(self.output_port)

    def validate_port(self, port: str) -> None:
        if not self.PORT_PATTERN.match(port):
            raise UnsupportedPortsInFilterError


class Filters:
    def __init__(self, logger: "Logger", table: str = None):
        self._logger = logger
        self.filters_list: List[Filter] = []

        if table is not None:
            self.update_filters_from_table(table)

    def __iter__(self):
        return iter(self.filters_list)

    def update_filters_from_table(self, table: str) -> None:
        """Update filters from show filters output."""
        lines = table.splitlines()
        try:
            dicts = table2dicts(lines[0], lines[1], lines[2:])
        except ParseTableError as e:
            raise ParseFilterError(f"Could not parse filters.") from e

        self.filters_list = []
        for dict_ in dicts:
            try:
                filter_ = Filter.from_dict(dict_)
            except UnsupportedPortsInFilterError:
                # fixme really?
                # fixme just ignore?
                self._logger.debug(
                    f"We support only one port in the filter. Line was: \n"
                    f"{dict_.original_line}"
                )
            else:
                self.filters_list.append(filter_)

    def get_connected_ports(self) -> Mapping[str, List[str]]:
        ports_connections: Mapping = defaultdict(list)

        for filter_ in self:
            ports_connections[filter_.input_port].append(filter_.output_port)

        return ports_connections


class L1Actions(BaseCgsActions):
    def connect_ports(self, src_port: str, dst_port: str):
        with self.enter_command_mode(ConfigCommandMode):
            self.execute_command(CONNECT_PORTS, src_port=src_port, dst_port=dst_port)

    def commit(self):
        self.execute_command(COMMIT)

    def get_filters(self) -> Filters:
        with self.enter_command_mode(EnableCommandMode):
            connections = self.execute_command(SHOW_CONNECTIONS, remove_prompt=True)

        return Filters(self._logger, connections)

    def get_connected_ports(self) -> Mapping[str, List[str]]:
        return self.get_filters().get_connected_ports()

    def get_port_connected_ports(self, port: str):
        return self.get_connected_ports().get(port, [])

    def get_filter_ids_with_ports_in_it(self, ports: List[str]) -> Iterator[str]:
        for filter_ in self.get_filters():
            if set(ports) & {filter_.input_port, filter_.output_port}:
                yield filter_.id

    def get_filters_with_src_and_dst_ports(
        self, src_port: str, dst_ports: List[str]
    ) -> Iterator[str]:
        for filter_ in self.get_filters():
            if filter_.input_port == src_port and filter_.output_port in dst_ports:
                yield filter_.id

    def remove_filters(self, filter_ids: Iterable[str]):
        """Remove filters.

        It's important to delete all needed filters in one command.
        After deleting a filter next filters change their ids
        """
        with self.enter_command_mode(ConfigCommandMode):
            str_ids = ",".join(filter_ids)
            self.execute_command(DELETE_FILTERS, filter_ids=str_ids)
