from cloudshell.devices.runners.connectivity_runner import ConnectivityRunner

from cloudshell.cgs.flows.add_vlan import CgsAddVlanFlow
from cloudshell.cgs.flows.remove_vlan import CgsRemoveVlanFlow


class CgsConnectivityRunner(ConnectivityRunner):
    @property
    def add_vlan_flow(self):
        """

        :return:
        """
        return CgsAddVlanFlow(self.cli_handler, self._logger)

    @property
    def remove_vlan_flow(self):
        """

        :return:
        """
        return CgsRemoveVlanFlow(self.cli_handler, self._logger)
