from cloudshell.cgs.cli.command_modes import EnableCommandMode, ConfigCommandMode
from cloudshell.cli.service.command_mode_helper import CommandModeHelper

from cloudshell.cli.configurator import AbstractModeConfigurator


class CGSCliConfigurator(AbstractModeConfigurator):

    def __init__(self, cli, resource_config, logger):
        super().__init__(resource_config, logger, cli)
        self.modes = CommandModeHelper.create_command_mode(resource_config)

    @property
    def enable_mode(self):
        return self.modes.get(EnableCommandMode)

    @property
    def config_mode(self):
        return self.modes.get(ConfigCommandMode)
