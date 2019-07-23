from logging import Logger
from unittest import TestCase
from unittest.mock import create_autospec

from cloudshell.cgs.cli.cli_configurator import CgsCliConfigurator, CliConfig
from cloudshell.cgs.cli.command_modes import EnableCommandMode, ConfigCommandMode


class TestCliConfigurator(TestCase):
    @staticmethod
    def get_cli_configurator():
        cli_config = CliConfig("test_user", "test_password", "example.com", "22", "ssh")
        logger = create_autospec(Logger)
        return CgsCliConfigurator(cli_config, logger)

    def test_getting_enable_mode(self):
        cli_configurator = self.get_cli_configurator()
        self.assertIsInstance(cli_configurator.enable_mode, EnableCommandMode)

    def test_getting_config_mode(self):
        cli_configurator = self.get_cli_configurator()
        self.assertIsInstance(cli_configurator.config_mode, ConfigCommandMode)
