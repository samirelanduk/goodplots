from unittest import TestCase
from unittest.mock import Mock, patch
from goodplots import Chart, Series

class ChartTest(TestCase):

    def setUp(self):
        self.series = [Mock(Series), Mock(Series), Mock(Series)]



class ChartCreationTests(ChartTest):

    def test_can_create_empty_chart(self):
        chart = Chart()
        self.assertEqual(chart._series, [])


    def test_can_create_chart_with_series(self):
        chart = Chart(self.series)
        self.assertEqual(chart._series, self.series)


    def test_series_must_be_iterable_of_series(self):
        with self.assertRaises(ValueError):
            Chart(100)
        with self.assertRaises(TypeError):
            Chart(["1", "2"])


    def test_can_create_chart_with_title(self):
        chart = Chart(self.series, title="Chart Title")
        self.assertEqual(chart._title, "Chart Title")



class ChartReprTests(ChartTest):

    def test_chart_repr(self):
        chart = Chart(self.series)
        self.assertEqual(repr(chart), "<Chart (3 series)>")
