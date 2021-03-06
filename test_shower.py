from SignalInjector import *
from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":
    sig = SignalInjector()
    sig.startShower(Location(55.5, 13.5), 25000, 0., 0.3, 0.2, 1e-6)
    for t in xrange(10):
        xs = []
        ys = []
        ws = []
        weightf = sig.getSignal()[0]
        for x in np.arange(55, 56, 0.01):
            for y in np.arange(13, 14, 0.01):
                w, _ = weightf(Location(x, y))
                xs.append(x)
                ys.append(y)
                ws.append(w)
        plt.scatter(xs,ys,c=ws)
        plt.colorbar()
        plt.show()
                
