
from ..utils.abstractCollection import AbstractCollection

class AbstractBag(AbstractCollection):


    def __init__(self, sourceCollection = None):
        """Sets the initial state of self,
            which includes the contents of sourceCollection,
            if it is present."""

        if type(self) == AbstractBag:
            raise NotImplementedError("Cannot create object of type AbstractBag")
        super().__init__(sourceCollection)
        
      
      
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True
    
                
      
   
    def count(self, target):
        counter = 0
        for item in self:
            if item == target:
                counter += 1
        
        return counter
    
    
if __name__ == '__main__':
    AB = AbstractBag()
    
    