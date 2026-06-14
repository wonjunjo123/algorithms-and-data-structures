"""
File: arrayPriorityQueue.py
Author: Wonjun Jo and AJ Thomas
"""

from .arrays import Array
from .abstractCollection import AbstractCollection
from .arrayQueue import ArrayQueue

class ArrayPriorityQueue(ArrayQueue):
    """An array-based priority queue implementation."""

    # Simulates a circlular priority queue within an array

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        super().__init__(sourceCollection)

    def add(self, item):
        """Inserts item in the queue according to priority."""
        
        if self._size >= len(self._items):
            self.resize(2)
            
        if self.isEmpty():
            self._rear = self._front = 0
            self._items[self._rear] = item
        else:
            targetIndex = self._front
            # while loops finds where item needs to go, the index equals targetIndex
            while item > self._items[targetIndex]:
                targetIndex += 1
                targetIndex %= len(self._items)
                if targetIndex == (self._rear + 1)%len(self._items): # if item should go at the very back, break
                    break
            # Now that we have targetIndex, we shift all the items back
            pointer = (self._rear + 1)%len(self._items) # points to the item (None) after self._rear
            while pointer != targetIndex:
                self._items[pointer] = self._items[len(self._items) - 1 if pointer == 0 else pointer - 1]
                pointer -= 1
                if pointer < 0:
                    pointer = len(self._items) - 1
            self._items[targetIndex] = item

            self._rear += 1
            self._rear %= len(self._items)


        self._size += 1
        self.incModCount()

