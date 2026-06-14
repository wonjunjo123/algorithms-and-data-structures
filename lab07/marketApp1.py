"""
File: marketapp1.py
Author: Ken Lambert

Terminal-based simulation of a supermarket checkout process.

Customer's processing time varies around the average,
so give it a random time between 1 and average time * 2 + 1.
"""

from marketModel import MarketModel

def main():
    print("Welcome to the Martket Simulator!\n")
    lengthOfSimulation = int(input("Enter the total running time: "))
    averageTimePerCus = int(input("Enter the average processing time per customer: "))
    probabilityOfNewArrival = float(input("Enter the probability of a new arrival: "))
    numCashiers = int(input("Enter the number of cashiers: "))
    if lengthOfSimulation < 1 or lengthOfSimulation > 1000:
        print("Running time must be an integer greater than 0" + \
              "\nand less than or equal to 1000")
    elif averageTimePerCus <= 0 or averageTimePerCus >= lengthOfSimulation:
        print("Average time per customer must be an integer" + \
              "\ngreater than 0 and less than running time")
    elif probabilityOfNewArrival <= 0 or probabilityOfNewArrival > 1:
        print("Probability must be geater than 0" + \
              "\nand less than or equal to 1")
    elif numCashiers <= 0:
        print("Number of cashiers must be >= 0")
    else:
        model = MarketModel(lengthOfSimulation, averageTimePerCus,
                            probabilityOfNewArrival, numCashiers)
        model.runSimulation()
        print("\n" + "-" * 40)
        print(model)

if __name__ == "__main__":
    main()

   
