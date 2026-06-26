"""
File: abstractlist.py
Author: YOUR NAME GOES HERE

Common data and method implementations for lists.
"""

from .abstractCollection import AbstractCollection

class AbstractList(AbstractCollection):
    """Represents an abstract list."""

    def __init__(self, sourceCollection):
        """Sets up the collection."""
        super().__init__(sourceCollection)

    def index(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        
        iterator = self.listIterator()
        itemIndex = 0
        
        iterator.first()
        
        while iterator.hasNext():
            if iterator.next() == item:
                return itemIndex
            
            itemIndex += 1
            
        ## Alternate version:
        #itemIndex = 0
        #for i in self:
        #    if i == item:
        #        return itemIndex
        #    
        #    itemIndex += 1
        
        
        raise ValueError("Item " + str(item) + " not in list.")
    
    def remove(self, item):
        """Precondition: item is in the list.
        Raises: ValueError if item in not in self.
        Postcondition: item is removed from self."""
        self.pop(self.index(item), item)
        

    def add(self, item):
        """Adds the item to the end of the list."""
        self.insert(len(self), item)
        

    def append(self, item):
        """Adds the item to the end of the list."""
        self.add(item)

    def listIterator(self):
        """Returns a list iterator."""
        raise NotImplementedError("Abstract class method invoked.")
