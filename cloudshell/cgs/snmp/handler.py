from cloudshell.devices.snmp_handler import SnmpHandler

from cloudshell.cgs.flows.disable_snmp import CgsDisableSnmpFlow
from cloudshell.cgs.flows.enable_snmp import CgsEnableSnmpFlow


class CgsSnmpHandler(SnmpHandler):
    def __init__(self, resource_config, logger, api, cli_handler):
        super(CgsSnmpHandler, self).__init__(resource_config, logger, api)
        self.cli_handler = cli_handler
        self.api = api

    def _create_enable_flow(self):
        return CgsEnableSnmpFlow(
            cli_handler=self.cli_handler,
            resource_config=self.resource_config,
            api=self.api,
            logger=self._logger,
        )

    def _create_disable_flow(self):
        return CgsDisableSnmpFlow(
            cli_handler=self.cli_handler,
            resource_config=self.resource_config,
            logger=self._logger,
        )
