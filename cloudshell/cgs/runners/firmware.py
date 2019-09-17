from cloudshell.devices.runners.firmware_runner import FirmwareRunner

from cloudshell.cgs.flows.load_firmware import CgsLoadFirmwareFlow


class CgsFirmwareRunner(FirmwareRunner):
    @property
    def load_firmware_flow(self):
        return CgsLoadFirmwareFlow(cli_handler=self.cli_handler, logger=self._logger)
