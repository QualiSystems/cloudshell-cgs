import typing
from dataclasses import dataclass

from cloudshell.cli.command_template.command_template_executor import (
    CommandTemplateExecutor,
)
from cloudshell.cli.configurator import AbstractModeConfigurator
from cloudshell.cli.service.cli_service_impl import CliServiceImpl
from cloudshell.cli.service.command_mode_helper import CommandModeHelper

from cloudshell.cgs.cli.command_modes import ConfigCommandMode, EnableCommandMode
from cloudshell.cgs.command_templates.configuration import DISABLE_PAGINATION

if typing.TYPE_CHECKING:
    from cloudshell.cli.service.cli import CLI
    from logging import Logger


@dataclass
class CliConfig:
    user: str
    password: str
    address: str
    cli_tcp_port: str
    cli_connection_type: str


class CgsCliConfigurator(AbstractModeConfigurator):
    def __init__(self, cli_config: CliConfig, logger: "Logger", cli: "CLI" = None):
        super().__init__(cli_config, logger, cli)
        self.modes = CommandModeHelper.create_command_mode()

    @property
    def enable_mode(self) -> EnableCommandMode:
        return self.modes.get(EnableCommandMode)

    @property
    def config_mode(self) -> ConfigCommandMode:
        return self.modes.get(ConfigCommandMode)

    def _on_session_start(self, session, logger):
        cli_service = CliServiceImpl(session, self.config_mode, logger)
        CommandTemplateExecutor(cli_service, DISABLE_PAGINATION).execute_command()
