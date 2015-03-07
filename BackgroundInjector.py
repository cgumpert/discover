class BackgroundInjector:
    def __init__(self,threshold=0.2):
        self._threshold = threshold

    def getBackground(self):
        return lambda loc : self._threshold
