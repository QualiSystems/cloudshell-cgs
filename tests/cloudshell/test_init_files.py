import os
import unittest

from tests.cloudshell.base_test import PACKAGE_DIR


class TestInitFiles(unittest.TestCase):
    def test_init_has_extend_path(self):
        """Test that don't forget to extend path.

        It need to correct work import cloudshell packages
        """
        for cur_dir, _, files in os.walk(PACKAGE_DIR):
            if "__init__.py" in files:
                path = os.path.join(cur_dir, "__init__.py")
                with open(path) as fo:
                    data = fo.read()

                self.assertIn("__path__ = extend_path(__path__, __name__)", data)
