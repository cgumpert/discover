import random

class BackgroundInjector:
    def __init__(self,threshold=0.2,intensity=0.05):
        self._threshold = threshold
        self._intensity = intensity

    def getBackground(self):
        return lambda loc : (self._threshold,random.expovariate(1./self._intensity))
