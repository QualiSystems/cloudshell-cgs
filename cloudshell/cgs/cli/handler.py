from cloudshell.cli.command_mode_helper import CommandModeHelper
from cloudshell.devices.cli_handler_impl import CliHandlerImpl

from cloudshell.cgs.cli.command_modes import (
    ConfigCommandMode,
    EnableCommandMode,
    SNMPConfigCommandMode,
    SwUpgradeConfigCommandMode,
)


class CgsCliHandler(CliHandlerImpl):
    def __init__(self, cli, resource_config, logger, api):
        super(CgsCliHandler, self).__init__(cli, resource_config, logger, api)
        self.modes = CommandModeHelper.create_command_mode(resource_config, api)

    @property
    def enable_mode(self):
        """Enable mode.

        :rtype: EnableCommandMode
        """
        return self.modes[EnableCommandMode]

    @property
    def config_mode(self):
        """Config mode.

        :rtype: ConfigCommandMode
        """
        return self.modes[ConfigCommandMode]

    @property
    def snmp_config_mode(self):
        """SNMP Config mode.

        :rtype: SNMPConfigCommandMode
        """
        return self.modes[SNMPConfigCommandMode]

    @property
    def sw_upgrade_config_mode(self):
        """SW Upgrade Config mode.

        :rtype: SNMPConfigCommandMode
        """
        return self.modes[SwUpgradeConfigCommandMode]

    def on_session_start(self, session, logger):
        """Perform some default commands when session just opened.

        :param session:
        :param logger:
        :return:
        """
        session.send_line("config", logger)
        session.send_line("system cli session paginate false", logger)
        session.send_line("commit", logger)
