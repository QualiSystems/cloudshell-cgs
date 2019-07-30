from typing import TYPE_CHECKING, Dict, Type

from cloudshell.cli.command_template.command_template_executor import (
    CommandTemplateExecutor,
)

if TYPE_CHECKING:
    from logging import Logger
    from cloudshell.cli.service.cli_service_impl import CliServiceImpl
    from cloudshell.cli.service.command_mode import CommandMode
    from cloudshell.cli.command_template.command_template import CommandTemplate


class BaseCgsActions:
    def __init__(
        self,
        cli_service: "CliServiceImpl",
        command_modes: Dict[Type["CommandMode"], CommandMode],
        logger: "Logger",
    ):
        self._cli_service = cli_service
        self._command_modes = command_modes
        self._logger = logger

    def execute_command(self, command_template: "CommandTemplate", **kwargs):
        return CommandTemplateExecutor(
            self._cli_service, command_template
        ).execute_command(**kwargs)

    def enter_command_mode(self, command_mode: Type["CommandMode"]):
        command_mode_instance = self._command_modes[command_mode]
        return self._cli_service.enter_mode(command_mode_instance)
