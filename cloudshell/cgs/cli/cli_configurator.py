from cloudshell.cli.command_template.command_template_executor import CommandTemplateExecutor
from cloudshell.cli.configurator import AbstractModeConfigurator
from cloudshell.cli.service.cli_service_impl import CliServiceImpl
from cloudshell.cli.service.command_mode_helper import CommandModeHelper

from cloudshell.cgs.cli.command_modes import ConfigCommandMode, EnableCommandMode
from cloudshell.cgs.command_templates.configuration_commands import (
    DISABLE_PAGINATION,
    COMMIT,
)


class CliConfig(object):
    def __init__(self, user, password, address, cli_tcp_port, cli_connection_type):
        """

        :param str user:
        :param str password:
        :param str address:
        :param str cli_tcp_port:
        :param str cli_connection_type:
        :return:
        """
        self.user = user
        self.password = password
        self.address = address
        self.cli_tcp_port = cli_tcp_port
        self.cli_connection_type = cli_connection_type


class CgsCliConfigurator(AbstractModeConfigurator):
    def __init__(self, cli_config, logger, cli=None):
        """

        :param CliConfig cli_config:
        :param logging.Logger logger:
        :param cloudshell.cli.service.cli.CLI cli:
        """
        super(CgsCliConfigurator, self).__init__(cli_config, logger, cli)
        self.modes = CommandModeHelper.create_command_mode()

    @property
    def enable_mode(self):
        """

        :rtype: EnableCommandMode
        """
        return self.modes.get(EnableCommandMode)

    @property
    def config_mode(self):
        """

        :rtype: ConfigCommandMode
        """
        return self.modes.get(ConfigCommandMode)

    def _on_session_start(self, session, logger):
        """

        :param session:
        :param logging.Logger logger:
        :return:
        """
        cli_service = CliServiceImpl(session, self.config_mode, logger)
        CommandTemplateExecutor(cli_service, DISABLE_PAGINATION).execute_command()
        CommandTemplateExecutor(cli_service, COMMIT).execute_command()
