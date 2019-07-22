import typing

from cloudshell.cgs.cli.cli_configurator import CliConfig

if typing.TYPE_CHECKING:
    from cloudshell.shell.standards.resource_config_generic_models import \
        GenericCLIConfig


class CliConfigResourceConfig(CliConfig):
    @classmethod
    def from_resource_config(cls, resource_config: 'GenericCLIConfig'):
        return cls(
            resource_config.user,
            resource_config.password,
            resource_config.address,
            resource_config.cli_tcp_port,
            resource_config.cli_connection_type,
        )
