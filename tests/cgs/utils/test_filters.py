from unittest import TestCase

import mock

from cloudshell.cgs.utils.filters import Filters


class TestFilters(TestCase):
    def setUp(self):
        self.filters = Filters(logger=mock.MagicMock())

    def test_find_filters_by_fields(self):
        self.filters.find_filters_by_fields()
