class Location:
    def __init__(self, x = 0, y = 0):
        self._x = x # longitude
        self._y = y # latitude

    @property
    def x(self):
        return float(self._x)

    @x.setter
    def x(self,value):
        self._x = float(value)

    @property
    def y(self):
        return float(self._y)

    @y.setter
    def y(self,value):
        self._y = float(value)

    def __str__(self):
        return "Location({0},{1}) <{2}>".format(self._x, self._y, hex(id(self)))

    def __repr__(self):
        return self.__str__()


