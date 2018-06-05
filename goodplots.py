
class Chart:

    def __init__(self):
        self._series = []



class Series:

    TYPES = ("line", "bar", "scatter")

    def __init__(self, data, type="line", name=""):
        data = list(data)
        try:
            iter(data[0])
            assert len(data[0]) == 2
        except:
            data = list(enumerate(data, start=1))

        if any(len(datum) != 2 for datum in data):
            raise ValueError(f"Data for series is not structured correctly")
        self._data = data

        if type not in self.TYPES:
            raise ValueError(f"Valid types are {self.TYPES} - not '{type}'")
        self._type = type
        self._name = name


    def __repr__(self):
        return "<{} Series {}{}>".format(
         self._type.title(),
         "'{}' ".format(self._name) if self._name else "",
         self._data)


    def __str__(self):
        return "<{} Series {}({} data points)>".format(
         self._type.title(),
         "'{}' ".format(self._name) if self._name else "",
         len(self._data))
