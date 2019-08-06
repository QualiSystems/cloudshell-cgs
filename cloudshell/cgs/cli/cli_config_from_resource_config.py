from cloudshell.cgs.cli.cli_configurator import CliConfig


class CliConfigResourceConfig(CliConfig):
    @classmethod
    def from_resource_config(cls, resource_config):
        """

        :param cloudshell.shell.standards.resource_config_generic_models.GenericCLIConfig resource_config:
        :rtype: CliConfigResourceConfig
        """
        return cls(
            resource_config.user,
            resource_config.password,
            resource_config.address,
            resource_config.cli_tcp_port,
            resource_config.cli_connection_type,
        )
