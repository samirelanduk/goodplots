from unittest import TestCase
from goodplots import Series

class SeriesCreationTests(TestCase):

    def test_can_create_series(self):
        series = Series([[1, "A"], [2, "B"]])
        self.assertEqual(series._data, [[1, "A"], [2, "B"]])
