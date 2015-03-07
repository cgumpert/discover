from Location import Location
from functools import partial

def shower_generator(angle, duration):
    for step in duration:
        yield step

class SignalInjector(object):
    def __init__(self):
        self._showers = []

    def getSignal(self):
        return [shower.next() for shower in self._showers]
            
    def startShower(self, angle, duration):
        self._showers.append(partial(shower_generator, angle, duration))
