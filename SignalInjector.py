from Location import Location

class ShowerGenerator(object):
    def __init__(self):
        pass


class SignalInjector(object):
    def __init__(self):
        self._showers = []

    def getSignal(self):
        return [shower.next() for shower in self._showers]
            
