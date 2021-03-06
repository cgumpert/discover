################################################################################
# Implementation of CarHandler
################################################################################

# python include(s)
import random
import numpy

# package include(s)
from CarModule import Car
from Location import Location


################################################################################
class CarHandler(object):
    #_______________________________________ 
    def __init__(self):
        self.__listOfCars = []
        self.__isInit = False
    
    #_______________________________________ 
    def __getitem__(self, idx):
        return self.__listOfCars[idx]
    
    #_______________________________________ 
    def __repr__(self):
        return self.__listOfCars.__repr__()
    
    #_______________________________________ 
    def __str__(self):
        return self.__listOfCars.__repr__()
    
    
    ########################################        
    # Signal Handling
    ######################################## 
    
    #_______________________________________ 
    def receiveSignal(self, *injectors):
        if not self.isInit():
            print "CarHandler not initialised"
            return

        for car in self.__listOfCars:
            self.__evalCar(car, *injectors)
            
    #_______________________________________ 
    def __evalCar(self, car, *injectors):
        sum_intens = 0
        
        for injector in injectors:
            prob, intens, isSignal = injector(car.getLocation())
            
            #if car.getID() == 1:
                #print "EvalCar: {0}, {1}".format(prob, intens)
                #self.__checkInjector(injector)

            if isSignal:
                #print "{0}: {1}".format(prob, intens)
                intens = prob

            if self.__evalProbValue(prob):
                sum_intens += intens
    
        car.receiveSignal(sum_intens)
    
    #_______________________________________ 
    def __evalProbValue(self, prob):
        rdn = random.random()
        if rdn <= prob:
            return True
        else:
            return False

    #_______________________________________ 
    def __checkInjector(self, injector):
        print "Call CheckInjector..."
        s = 50.9591
        w = 13.5770
        n = 51.1024
        e = 13.8963

        xv = numpy.linspace(w, e, 10)
        yv = numpy.linspace(s, n, 10)

        for x in xv:
            for y in yv:
                prob, intens, isSignal = injector(Location(x,y))
                print "\t({0},{1},{2}): {3}, {4}".format(x,y,isSignal,prob,intens)


    ########################################        
    # Getter
    ######################################## 

    #_______________________________________ 
    def getCarList(self):
        return self.__listOfCars


    ########################################        
    # Initialisation
    ######################################## 
    
    #_______________________________________ 
    def clear(self):
        self.__listOfCars = []
        self.__isInit = False
    
    #_______________________________________ 
    def isInit(self): return self.__isInit
    
    #_______________________________________ 
    def initialise(self, locationList):
        try:
            self.clear()
            for location in locationList:
                self.__listOfCars.append(Car(locationList.index(location),
                                             location)
                                        )
       
            self.__isInit = True
        
        except:
            print "CarHandler - Error during initialisation"
            self.clear()
            raise





