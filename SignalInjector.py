from Location import Location
from functools import partial


class ShowerGenerator(object):
    def __init__(self, angle, duration):
        self._angle = angle
        self._duration = duration
        self._step = 0
        
    def nextStep(self):
        if self._step == self._duration:
            return None
        self._step += 1
        return lambda loc: (0.3*loc.x, 0.4*loc.y)
        

class SignalInjector(object):
    def __init__(self):
        self._showers = []

    def getSignal(self):
        return [shower for shower in [shower.nextStep() for shower in self._showers] if shower is not None]
            
    def startShower(self, angle, duration):
        self._showers.append(ShowerGenerator(angle, duration))
