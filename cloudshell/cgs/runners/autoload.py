from cloudshell.devices.runners.autoload_runner import AutoloadRunner


class AbstractCgsAutoloadRunner(AutoloadRunner):
    def __init__(self, logger, resource_config, snmp_handler):
        """Init command.

        :param logger:
        :param resource_config:
        :param snmp_handler:
        """
        super(AbstractCgsAutoloadRunner, self).__init__(
            resource_config=resource_config, logger=logger
        )
        self.snmp_handler = snmp_handler
