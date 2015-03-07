class Location:
    def __init__(self):
        self._x = 0
        self._y = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,value):
        self._y = value        
