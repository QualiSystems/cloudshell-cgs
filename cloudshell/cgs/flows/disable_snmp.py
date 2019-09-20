from cloudshell.cli.session.session_exceptions import CommandExecutionException
from cloudshell.devices.flows.cli_action_flows import DisableSnmpFlow
from cloudshell.snmp.snmp_parameters import SNMPV2WriteParameters, SNMPV3Parameters

from cloudshell.cgs.command_actions.commit import CommitActions
from cloudshell.cgs.command_actions.snmpv2 import SnmpV2Actions
from cloudshell.cgs.command_actions.snmpv3 import SnmpV3Actions


class CgsDisableSnmpFlow(DisableSnmpFlow):
    def __init__(self, cli_handler, resource_config, logger):
        """Init command.

        :param cli_handler:
        :param resource_config:
        :param logger:
        """
        super(CgsDisableSnmpFlow, self).__init__(cli_handler=cli_handler, logger=logger)
        self._resource_config = resource_config

    def execute_flow(self, snmp_parameters):
        """Execute disable SNMP flow.

        :param cloudshell.snmp.snmp_parameters.SNMPParameters snmp_parameters:
        :return: commands output
        """
        with self._cli_handler.get_cli_service(
            self._cli_handler.snmp_config_mode
        ) as cli_service:
            if isinstance(snmp_parameters, SNMPV3Parameters):
                disable_snmp = self._disable_snmp_v3
            else:
                disable_snmp = self._disable_snmp_v2

            disable_snmp(cli_service=cli_service, snmp_parameters=snmp_parameters)

    def _disable_snmp_v2(self, cli_service, snmp_parameters):
        """Execute disable SNMPv2 flow.

        :param cloudshell.cli.cli_service_impl.CliServiceImpl cli_service:
        :param cloudshell.snmp.snmp_parameters.SNMPParameters snmp_parameters:
        :return: commands output
        """
        snmp_community = snmp_parameters.snmp_community

        if not snmp_community:
            raise Exception("SNMP community can not be empty")

        snmp_v2_actions = SnmpV2Actions(cli_service=cli_service, logger=self._logger)
        commit_actions = CommitActions(cli_service=cli_service, logger=self._logger)

        try:
            output = snmp_v2_actions.disable_snmp()

            if isinstance(snmp_parameters, SNMPV2WriteParameters):
                output += snmp_v2_actions.unset_write_community(
                    snmp_community=snmp_community
                )
            else:
                output += snmp_v2_actions.unset_read_community(
                    snmp_community=snmp_community
                )

            output += commit_actions.commit()

        except CommandExecutionException:
            self._logger.exception("Failed to disable SNMPv2 on the device:")
            commit_actions.abort()
            raise

        return output

    def _disable_snmp_v3(self, cli_service, snmp_parameters):
        """Execute disable SNMPv3 flow.

        :param cloudshell.cli.cli_service_impl.CliServiceImpl cli_service:
        :param cloudshell.snmp.snmp_parameters.SNMPParameters snmp_parameters:
        :return: commands output
        """
        snmp_v3_actions = SnmpV3Actions(cli_service, self._logger)
        commit_actions = CommitActions(cli_service=cli_service, logger=self._logger)

        try:
            output = snmp_v3_actions.disable_snmp()
            output += snmp_v3_actions.remove_snmp_user(
                snmp_user=snmp_parameters.snmp_user
            )
            output += commit_actions.commit()

        except CommandExecutionException:
            commit_actions.abort()
            self._logger.exception("Failed to Enable SNMPv3 on the device:")
            raise

        return output
