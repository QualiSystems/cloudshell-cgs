import re
from collections import defaultdict

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


class Filter(object):
    ADMIN_ENABLED = "enabled"
    ACTION_REDIRECT = "redirect"
    PORT_PATTERN = re.compile(r"^\d+(/\d+)?$")

    def __init__(self, filter_id, admin, action, input_port, output_port):
        """

        :param str filter_id:
        :param str admin:
        :param str action:
        :param str input_port:
        :param str output_port:
        """
        self.filter_id = filter_id
        self.admin = admin
        self.action = action
        self.input_port = input_port
        self.output_port = output_port
        self.validate()

    @classmethod
    def from_dict(cls, data):
        """

        :param dict data:
        :return:
        """
        return cls(
            filter_id=data["Filter"],
            admin=data["Admin"],
            action=data["Action"],
            input_port=data["Input"],
            output_port=data["Output"],
        )

    @property
    def is_enabled(self):
        """

        :rtype: bool
        """
        return self.admin.lower() == self.ADMIN_ENABLED

    @property
    def is_redirect(self):
        """

        :rtype: bool
        """
        return self.action.lower() == self.ACTION_REDIRECT

    def validate(self):
        """

        :return:
        """
        self.validate_port(self.input_port)
        self.validate_port(self.output_port)

    def validate_port(self, port):
        """

        :param str port:
        :return:
        """
        if not self.PORT_PATTERN.match(port):
            raise UnsupportedPortsInFilterError


class Filters(object):
    def __init__(self, logger, table=None):
        """

        :param logging.Logger logger:
        :param str table:
        """
        self._logger = logger
        self.filters_list = []

        if table is not None:
            self.update_filters_from_table(table)

    def __iter__(self):
        return iter(self.filters_list)

    def update_filters_from_table(self, table):
        """Update filters from show filters output

        :param str table:
        :return:
        """
        lines = table.splitlines()
        try:
            dicts = table2dicts(lines[0], lines[1], lines[2:])
        except ParseTableError as e:
            raise ParseFilterError("Could not parse filters") from e

        self.filters_list = []
        for dict_ in dicts:
            try:
                filter_ = Filter.from_dict(dict_)
            except UnsupportedPortsInFilterError:
                # fixme really?
                # fixme just ignore?
                self._logger.debug(
                    "We support only one port in the filter. Line was: \n {}".format(dict_.original_line)
                )
            else:
                self.filters_list.append(filter_)

    def get_connected_ports(self):
        """

        :rtype: dict[str, list[str]]
        """
        ports_connections = defaultdict(list)

        for filter_ in self:
            ports_connections[filter_.input_port].append(filter_.output_port)

        return ports_connections


class L1Actions(BaseCgsActions):
    def connect_ports(self, src_port, dst_port):
        """

        :param str src_port:
        :param str dst_port:
        :return:
        """
        with self.enter_command_mode(ConfigCommandMode):
            self.execute_command(CONNECT_PORTS, src_port=src_port, dst_port=dst_port)

    def commit(self):
        """

        :return:
        """
        self.execute_command(COMMIT)

    def get_filters(self):
        """

        :rtype: Filters
        """
        with self.enter_command_mode(EnableCommandMode):
            connections = self.execute_command(SHOW_CONNECTIONS, remove_prompt=True)

        return Filters(self._logger, connections)

    def get_connected_ports(self):
        """

        :rtype: dict[str, list[str]]
        """
        return self.get_filters().get_connected_ports()

    def get_port_connected_ports(self, port):
        """

        :param str port:
        :return:
        """
        return self.get_connected_ports().get(port, [])

    def get_filter_ids_with_ports_in_it(self, ports):
        """

        :param list[str] ports:
        :rtype: collections.Iterable[str]
        """
        for filter_ in self.get_filters():
            if set(ports) & {filter_.input_port, filter_.output_port}:
                yield filter_.id

    def get_filters_with_src_and_dst_ports(self, src_port, dst_ports):
        """

        :param str src_port:
        :param list[str] dst_ports:
        :rtype: collections.Iterable[str]
        """
        for filter_ in self.get_filters():
            if filter_.input_port == src_port and filter_.output_port in dst_ports:
                yield filter_.id

    def remove_filters(self, filter_ids):
        """Remove filters

        It's important to delete all needed filters in one command.
        After deleting a filter next filters change their ids
        :param collections.Iterable[str] filter_ids:
        :return:
        """
        with self.enter_command_mode(ConfigCommandMode):
            str_ids = ",".join(filter_ids)
            self.execute_command(DELETE_FILTERS, filter_ids=str_ids)
