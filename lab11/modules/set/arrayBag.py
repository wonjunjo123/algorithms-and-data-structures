"""
Author: YOUR NAME GOES HERE
File: arraybag.py
"""

from ..utils.arrays import Array
from .abstractBag import AbstractBag

class ArrayBag(AbstractBag):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        self.storeCurrentModCount()
        while cursor < len(self):
            yield self._items[cursor]
            if self.modCountChanged():
                raise AttributeError("Don't modify in an iterator loop!")
            cursor += 1


    
    
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.resetSizeAndModCount()
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
    
    def grow(self):
        newItems = Array(len(self._items) * 2)
        index = 0
        for item in self:
            newItems[index] = item
            index += 1
        
        self._items = newItems
    
    def shrink(self):
        if len(self._items) // 2 >= ArrayBag.DEFAULT_CAPACITY:
            newItems = Array(len(self._items) // 2)
            index = 0
            for item in self:
                newItems[index] = item
                index += 1
            
            self._items = newItems
            

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        
        if len(self) == len(self._items):
            self.grow()
        
        self._items[len(self)] = item
        self._size += 1
        
        self.incModCount()

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # Decrement logical size
        self._size -= 1
        # Check array memory here and decrease it if necessary
        
        if len(self) == len(self._items) // 4:
            self.shrink()
        
        self.incModCount()
        
        
