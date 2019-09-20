from cloudshell.devices.runners.state_runner import StateRunner

from cloudshell.cgs.flows.shutdown import CgsShutdownFlow


class CgsStateRunner(StateRunner):
    @property
    def shutdown_flow(self):
        return CgsShutdownFlow(cli_handler=self.cli_handler, logger=self._logger)

    def shutdown(self):
        return self.shutdown_flow.execute_flow()
