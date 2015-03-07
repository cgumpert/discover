import random

class BackgroundInjector:
    def __init__(self,threshold=0.4,intensity=0.1):
        self._threshold = threshold
        self._intensity = intensity

    def getBackground(self):
        return lambda loc : (self._threshold,random.expovariate(1./self._intensity))
