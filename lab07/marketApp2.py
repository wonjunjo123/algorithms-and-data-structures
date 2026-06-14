"""
File: marketapp2.py
Author: Ken Lambert

GUI-based simulation of a supermarket checkout process.
"""

from utils.breezypythongui import EasyFrame
from marketModel import MarketModel

class MarketView(EasyFrame):
    """View of the simulation."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Market Simulator")
        self.addLabel(text = "Total running time",
                      row = 0, column = 0)
        self.addLabel(text = "Average processing time per customer",
                      row = 1, column = 0)
        self.addLabel(text = "Probablity of new arrival",
                      row = 2, column = 0)
        self.addLabel(text = "Number of cashiers",
                      row = 3, column = 0)
        self.addLabel(text = "Results",
                      row = 5, column = 0, columnspan = 2, sticky = "NSEW")
        self.runTimeFld = self.addIntegerField(value = 0, width = 5,
                                               row = 0, column = 1)
        self.aveTimeFld = self.addIntegerField(value = 0, width = 5,
                                               row = 1, column = 1)
        self.probabilityFld = self.addFloatField(value = 0.0, width = 5,
                                                 row = 2, column = 1)
        self.cashiersFld = self.addIntegerField(value = 0, width = 5,
                                                row = 3, column = 1)
        self.outputArea = self.addTextArea("", row = 6, column = 0,
                                           columnspan = 2,
                                           width = 40, height = 10)
        self.runBtn = self.addButton(text = "Run", row = 4, column = 0,
                                     columnspan = 2,
                                     command = self.run)
    # Event handling method.
    def run(self):
        """Obtains the inputs, validates them, runs the simulation,
        and displays the results."""
        # Obtain and validate the inputs
        lengthOfSimulation = self.runTimeFld.getNumber()
        averageTimePerCus = self.aveTimeFld.getNumber()
        probabilityOfNewArrival = self.probabilityFld.getNumber()
        numCashiers = self.cashiersFld.getNumber()
        if lengthOfSimulation == 0 or averageTimePerCus == 0 \
           or probabilityOfNewArrival == 0 or numCashiers == 0:
            self.messageBox("ERROR", "All inputs must be greater than 0")
            return

        # Create and run the simulation
        model = MarketModel(lengthOfSimulation, averageTimePerCus,
                            probabilityOfNewArrival, numCashiers)
        model.runSimulation()

        # Display the results
        self.outputArea.setText(str(model))

if __name__ == "__main__":
    MarketView().mainloop()
   
