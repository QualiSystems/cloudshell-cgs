import re

from cloudshell.cli.session.session_exceptions import CommandExecutionException
from cloudshell.devices.flows.cli_action_flows import AddVlanFlow

from cloudshell.cgs.command_actions.commit import CommitActions
from cloudshell.cgs.command_actions.vlan import VlanActions


class CgsAddVlanFlow(AddVlanFlow):
    @staticmethod
    def _get_port_name(full_port_name):
        """Parse CGS port name from the CS full port name.

        :param full_port_name:
        :return:
        """
        return re.sub("[^0-9]", "", full_port_name.split("/")[-1])

    def execute_flow(self, vlan_range, port_mode, port_name, qnq, c_tag):
        """Execute Add VLAN flow.

        :param vlan_range:
        :param port_mode:
        :param port_name:
        :param qnq:
        :param c_tag:
        :return:
        """
        port = self._get_port_name(full_port_name=port_name)

        with self._cli_handler.get_cli_service(
            self._cli_handler.config_mode
        ) as cli_service:
            vlan_actions = VlanActions(cli_service=cli_service, logger=self._logger)
            commit_actions = CommitActions(cli_service=cli_service, logger=self._logger)

            try:
                if qnq:
                    raise Exception("Shell doesn't support QinQ")

                if port_mode == "trunk":
                    output = vlan_actions.add_trunk_vlan_filter(
                        port=port, vlan_range=vlan_range
                    )
                else:
                    output = vlan_actions.add_access_vlan_filter(
                        port=port, vlan=vlan_range
                    )

                output += commit_actions.commit()

            except CommandExecutionException:
                self._logger.exception("Failed to add VLAN:")
                commit_actions.abort()
                raise

            return output
