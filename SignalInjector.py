from Location import Location

class SignalInjector(object):
    def __init__(self):
        pass

    def getSignal(self):
        return lambda loc : loc.x
