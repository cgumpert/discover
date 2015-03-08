
class ClockClass(object):
    def __init__(self, end = -1):
        self._time = 0
        self._end = end
        
    @property
    def time(self):
        return self._time

    def reset(self):
        self._time = 0
        
    def setEnd(self, end):
        self._end = end
        
    def __iter__(self):
        return self

    def next(self):
        if self._time == self._end:
            raise StopIteration()
        self._time += 1
        return self._time


clock = ClockClass()
