from cloudshell.cgs.cli.cli_configurator import CliConfig


class CliConfigForL1(CliConfig):
    @classmethod
    def from_runtime_config(cls, runtime_config, user, password, resource_address):
        """

        :param cloudshell.layer_one.core.helper.runtime_configuration.RuntimeConfiguration runtime_config:
        :param str user:
        :param str password:
        :param str resource_address:
        :rtype: CliConfigForL1
        """
        return cls(
            user,
            password,
            resource_address,
            runtime_config.read_key("CLI.PORTS"),
            runtime_config.read_key("CLI.TYPE"),
        )
