from unittest import TestCase
from goodplots import Chart

class ChartCreationTests(TestCase):

    def test_can_create_empty_chart(self):
        chart = Chart()
        self.assertEqual(chart._series, [])
