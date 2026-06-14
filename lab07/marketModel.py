"""
File: model.py
Author: Ken Lambert

Models multiple cashiers.
"""

from cashier import Cashier
from customer import Customer
import random

class MarketModel(object):

    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival, numCashiers):
        self._probabilityOfNewArrival = probabilityOfNewArrival
        self._lengthOfSimulation = lengthOfSimulation
        self._averageTimePerCus = averageTimePerCus
        self._cashiers = list()
        for x in range(0, numCashiers):
            self._cashiers.append(Cashier(x+1))
        
   
    def runSimulation(self):
        """Run the clock for n ticks."""
        for currentTime in range(self._lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self._probabilityOfNewArrival,
                currentTime,
                self._averageTimePerCus)
            
            # if successfully generated, send a customer to a cashier
            if customer != None:
                rand = random.randint(0, len(self._cashiers) - 1)
                shortest = rand # variable to keep track of cashier index with shortest line
                for x in range(rand-2, rand+3): # for the cashier indices within +-2 of the initial cashier
                    if x >= 0 and x < len(self._cashiers):
                        if self._cashiers[x].customersInLine() < self._cashiers[shortest].customersInLine():
                            shortest = x
                self._cashiers[shortest].addCustomer(customer)

            # Tell all cashiers to provide another unit of service
            for cashier in self._cashiers:
                cashier.serveCustomers(currentTime)

    def __str__(self):
        """Returns the string rep of the results of the simulation."""
        result = ''
        for cashier in self._cashiers:
            result += str(cashier) + '\n'
            
        return "CASHIER CUSTOMERS   AVERAGE     LEFT IN\n" + \
               "        PROCESSED   WAIT TIME   LINE\n" + \
               result
