import sys
from CarHandlerModule import CarHandler
from Location import Location
from SignalInjector import SignalInjector
from BackgroundInjector import BackgroundInjector
from Clock import clock

def main(argv):
    car_handler = CarHandler()
    car_handler.initialise([Location(3,3), Location(5,5)])
    sig_injector = SignalInjector()
    bgk_injector = BackgroundInjector()
    clock.setEnd(1000)
    for _ in clock:
        signals = sig_injector.getSignal()
        background = bgk_injector.getBackground()
        combine = [background]+signals
        car_handler.receiveSignal(*combine)
    

if __name__ == "__main__":
    main(sys.argv[1:])
