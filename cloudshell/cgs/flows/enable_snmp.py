from cloudshell.cli.session.session_exceptions import CommandExecutionException
from cloudshell.devices.flows.cli_action_flows import EnableSnmpFlow
from cloudshell.snmp.snmp_parameters import SNMPV2WriteParameters, SNMPV3Parameters

from cloudshell.cgs.cli.command_modes import SNMPv3UserConfigCommandMode
from cloudshell.cgs.command_actions.commit import CommitActions
from cloudshell.cgs.command_actions.snmpv2 import SnmpV2Actions
from cloudshell.cgs.command_actions.snmpv3 import SnmpV3Actions


class CgsEnableSnmpFlow(EnableSnmpFlow):
    SNMP_WAITING_TIMEOUT = 5 * 60
    SNMP_WAITING_INTERVAL = 5

    def __init__(self, cli_handler, resource_config, api, logger):
        """Init command.

        :param cli_handler:
        :param resource_config:
        :param api:
        :param logger:
        """
        super(CgsEnableSnmpFlow, self).__init__(cli_handler=cli_handler, logger=logger)
        self._resource_config = resource_config
        self._api = api

    def execute_flow(self, snmp_parameters):
        """Execute enable SNMP flow.

        :param cloudshell.snmp.snmp_parameters.SNMPParameters snmp_parameters:
        :return: commands output
        """
        with self._cli_handler.get_cli_service(
            self._cli_handler.snmp_config_mode
        ) as cli_service:
            if isinstance(snmp_parameters, SNMPV3Parameters):
                enable_snmp = self._enable_snmp_v3
            else:
                enable_snmp = self._enable_snmp_v2

            enable_snmp(cli_service=cli_service, snmp_parameters=snmp_parameters)

    def _enable_snmp_v2(self, cli_service, snmp_parameters):
        """Execute enable SNMPv2 flow.

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
            output = snmp_v2_actions.enable_snmp()

            if isinstance(snmp_parameters, SNMPV2WriteParameters):
                output += snmp_v2_actions.set_write_community(
                    snmp_community=snmp_community
                )
            else:
                output += snmp_v2_actions.set_read_community(
                    snmp_community=snmp_community
                )

            output += commit_actions.commit()

        except CommandExecutionException:
            self._logger.exception("Failed to enable SNMPv2 on the device:")
            commit_actions.abort()
            raise

        return output

    def _enable_snmp_v3(self, cli_service, snmp_parameters):
        """Execute enable SNMPv3 flow.

        :param cloudshell.cli.cli_service_impl.CliServiceImpl cli_service:
        :param cloudshell.snmp.snmp_parameters.SNMPParameters snmp_parameters:
        :return: commands output
        """
        snmp_v3_actions = SnmpV3Actions(cli_service=cli_service, logger=self._logger)
        commit_actions = CommitActions(cli_service=cli_service, logger=self._logger)

        try:
            output = snmp_v3_actions.enable_snmp()
            with cli_service.enter_mode(
                SNMPv3UserConfigCommandMode(
                    resource_config=self._resource_config,
                    api=self._api,
                    username=snmp_parameters.snmp_user,
                    parent_mode=cli_service.command_mode,
                )
            ):
                output += snmp_v3_actions.add_snmp_user_auth_and_priv(
                    snmp_password=snmp_parameters.snmp_password,
                    snmp_priv_key=snmp_parameters.snmp_private_key,
                    snmp_auth_proto=snmp_parameters.auth_protocol,
                    snmp_priv_proto=snmp_parameters.private_key_protocol,
                )

                output += commit_actions.commit()

        except CommandExecutionException:
            commit_actions.abort()
            self._logger.exception("Failed to enable SNMPv3 on the device:")
            raise

        return output
