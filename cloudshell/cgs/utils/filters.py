import re

from cloudshell.cgs.errors import UnsupportedPortsInFilterError
from cloudshell.cgs.utils.table2dicts import ConsoleTable


class Filters(ConsoleTable):
    class Model(ConsoleTable.Model):
        """Model that represents table row."""

        ADMIN_ENABLED = "enabled"
        ACTION_REDIRECT = "redirect"
        PORT_PATTERN = re.compile(r"^\d+(/\d+)?|all$")

        def __init__(
            self,
            filter_id,
            name,
            admin,
            action,
            input_port,
            output_port,
            classifiers,
            packet_processing,
        ):
            """Init command.

            :param str filter_id:
            :param str admin:
            :param str action:
            :param str input_port:
            :param str output_port:
            """
            self.filter_id = filter_id
            self.name = name
            self.admin = admin
            self.action = action
            self.input_port = input_port
            self.output_port = output_port
            self.classifiers = classifiers
            self.packet_processing = packet_processing
            self.validate()

        @classmethod
        def from_dict(cls, data):
            """Create instance from dict.

            :param dict data:
            :return:
            """
            return cls(
                filter_id=data["Filter"],
                name=data["Name"],
                admin=data["Admin"],
                action=data["Action"],
                input_port=data["Input"],
                output_port=data["Output"],
                classifiers=data["Classifiers"],
                packet_processing=data["Packet Processing"],
            )

        @property
        def is_enabled(self):
            """Check if enabled.

            :rtype: bool
            """
            return self.admin.lower() == self.ADMIN_ENABLED

        @property
        def is_redirect(self):
            """Check if redirect.

            :rtype: bool
            """
            return self.action.lower() == self.ACTION_REDIRECT

        def validate(self):
            """Validate filter data.

            :return:
            """
            self.validate_port(self.input_port)
            self.validate_port(self.output_port)

        def validate_port(self, port):
            """Validate port.

            :param str port:
            :return:
            """
            if not self.PORT_PATTERN.match(port):
                raise UnsupportedPortsInFilterError

    def find_filters_by_fields(self, **kwargs):
        """Find filters by their fields data.

        :param kwargs:
        :return:
        """
        return [
            filter_.filter_id
            for filter_ in self
            if all(
                (getattr(filter_, key) == value for key, value in kwargs.iteritems())
            )
        ]
