################################################################################
# Implementation of CarHandler
################################################################################

# python include(s)
import random

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
            prob, intens = injector(car.getLocation())
            
            if self.__evalProbValue(prob):
                is_hit = True
                sum_intens += intens
    
        car.receiveSignal(intens)
    
    #_______________________________________ 
    def __evalProbValue(self, prob):
        rdn = random.random()
        if prob <= rdn:
            return True
        else:
            return False

    
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

    #_______________________________________ 
    
    
    #_______________________________________ 
    #_______________________________________ 
    





