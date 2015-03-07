from Location import Location

def shower_generator(angle, duration):
    for step in duration:
        yield step

class SignalInjector(object):
    def __init__(self):
        self._showers = []

    def getSignal(self):
        return [shower.next() for shower in self._showers]
            
    def startShower(self, angle, duration):
        
