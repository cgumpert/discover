import sys
from CarHandlerModule import CarHandler
from Location import Location
from SignalInjector import SignalInjector
from BackgroundInjector import BackgroundInjector
from Clock import clock

def main(argv):
    car_handler = CarHandler()
    sig_injector = SignalInjector()
    bgk_injector = BackgroundInjector()
    clock.setEnd(10)
    for _ in clock:
        signals = sig_injector.getSignal()
        background = bgk_injector.getBackground()
        car_handler.receiveSignal(background, signals)
    

if __name__ == "__main__":
    main(sys.argv[1:])
