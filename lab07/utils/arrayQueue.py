"""
File: arrayQueue.py
Author: Wonjun Jo and AJ Thomas
"""

from .arrays import Array
from .abstractCollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circlular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._rear = self._front = -1
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        # Same as an iterator for an arrayBag, only using modulo inside self._items access
        #  to wrap the cursor around the end of the array
        cursor = self._front
        modCount = self.getModCount()
        a = len(self._items)
        while cursor < self._front + self._size:
            yield self._items[cursor%a]
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed in a for loop")
            cursor += 1
        

    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        
        return self._items[self._front]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.resetSizeAndModCount()
        self._rear = self._front = -1
        

    def resize(self, sizeFactor):
        # Only shrink if we're not too small
        newArray = Array(int(len(self._items)*sizeFactor))
        counter = 0
        for item in self:
            newArray[counter] = item
            counter += 1

        self._items = newArray
        self._front = 0
        self._rear = self._size - 1
        
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        
        if self._size >= len(self._items):
            self.resize(2)
            
        if self.isEmpty():
            self._rear = self._front = 0
        else:
            self._rear += 1
            self._rear %= len(self._items)

        self._items[self._rear] = item
        self._size += 1
        self.incModCount()

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        
        if self.isEmpty():
            raise KeyError('Queue is empty')
        
        data = self._items[self._front]
        self._size -= 1
        self.incModCount()

        if self.isEmpty():
            self._front = self._rear = -1
        else:
            self._front += 1
            self._front %= len(self._items)
            
        if self._size <= len(self._items)//4:
            self.resize(0.5)

        return data

        
         
