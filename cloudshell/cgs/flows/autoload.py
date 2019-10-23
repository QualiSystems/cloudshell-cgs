from cloudshell.devices.flows.snmp_action_flows import AutoloadFlow


class AbstractCgsSnmpAutoloadFlow(AutoloadFlow):
    @property
    def snmp_autoload_class(self):
        raise NotImplementedError(
            "Class {} must implement property 'snmp_autoload_class'".format(type(self))
        )

    def execute_flow(self, supported_os, shell_name, shell_type, resource_name):
        """Execute Autoload flow.

        :param supported_os:
        :param shell_name:
        :param shell_type:
        :param resource_name:
        :return:
        """
        with self._snmp_handler.get_snmp_service() as snmp_service:
            snmp_autoload = self.snmp_autoload_class(
                snmp_handler=snmp_service,
                shell_name=shell_name,
                shell_type=shell_type,
                resource_name=resource_name,
                logger=self._logger,
            )

            return snmp_autoload.discover(supported_os)
