from cloudshell.devices.flows.cli_action_flows import ShutdownFlow


class CgsShutdownFlow(ShutdownFlow):
    def execute_flow(self):
        raise Exception("Shell doesn't support 'Shutdown command'")
