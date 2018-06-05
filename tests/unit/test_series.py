from unittest import TestCase
from goodplots import Series

class SeriesCreationTests(TestCase):

    def test_can_create_series(self):
        series = Series([[0, 0], [1, 1], [2, 4]])
        self.assertEqual(series._data, [[0, 0], [1, 1], [2, 4]])
        self.assertEqual(series._type, "line")


    def test_can_enumerate_basic_iterable(self):
        series = Series([10, 20])
        self.assertEqual(series._data, [(1, 10), (2, 20)])


    def test_data_must_be_structured_correctly(self):
        with self.assertRaises(ValueError):
            Series([[10, "A"], ["B"]])
        with self.assertRaises(ValueError):
            Series([[10, "A"], ["A", "B", "C"]])


    def test_can_create_series_with_type(self):
        series = Series([[0, 0], [1, 1], [2, 4]], type="bar")
        self.assertEqual(series._type, "bar")


    def test_can_create_series_type_must_be_valid(self):
        with self.assertRaises(ValueError):
            Series([[0, 0], [1, 1], [2, 4]], type="blib")


    def test_can_create_series_with_name(self):
        series = Series([[0, 0], [1, 1], [2, 4]], name="series 2")
        self.assertEqual(series._name, "series 2")



class SeriesReprTests(TestCase):

    def test_series_repr(self):
        series = Series([[0, 0], [1, 1], [2, 4]])
        self.assertEqual((repr(series)), "<Line Series [[0, 0], [1, 1], [2, 4]]>")


    def test_series_repr_with_name(self):
        series = Series([[0, 0], [1, 1], [2, 4]], name="S2")
        self.assertEqual((repr(series)), "<Line Series 'S2' [[0, 0], [1, 1], [2, 4]]>")



class SeriesStrTests(TestCase):

    def test_series_str(self):
        series = Series([[0, 0], [1, 1], [2, 4]])
        self.assertEqual((str(series)), "<Line Series (3 data points)>")


    def test_series_str_with_name(self):
        series = Series([[0, 0], [1, 1], [2, 4]], name="S2")
        self.assertEqual((str(series)), "<Line Series 'S2' (3 data points)>")
