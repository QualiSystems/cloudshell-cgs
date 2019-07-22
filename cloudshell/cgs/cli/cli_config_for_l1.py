import typing

from cloudshell.cgs.cli.cli_configurator import CliConfig

if typing.TYPE_CHECKING:
    from cloudshell.layer_one.core.helper.runtime_configuration import \
        RuntimeConfiguration


class CliConfigForL1(CliConfig):
    @classmethod
    def from_runtime_config(
            cls,
            runtime_config: 'RuntimeConfiguration',
            user: str,
            password: str,
            resource_address: str,
    ):
        return cls(
            user,
            password,
            resource_address,
            runtime_config.read_key('CLI.PORTS'),
            runtime_config.read_key('CLI.TYPE'),
        )
