
class Chart:

    def __init__(self):
        self._series = []



class Series:

    TYPES = ("line", "bar", "scatter")

    def __init__(self, data, type="line", name=""):
        if len(data[0]) != 2:
            self._data = list(enumerate(data, start=1))
        else:
            if any(len(datum) != 2 for datum in data):
                raise ValueError(f"Data for series is not structured correctly")
            self._data = data
        if type not in self.TYPES:
            raise ValueError(f"Valid types are {self.TYPES} - not '{type}'")
        self._type = type
        self._name = name
