"""
File: linkedStack.py
Author: YOUR NAME GOES HERE
"""

from .abstractStack import AbstractStack
from .node import Node

class LinkedStack(AbstractStack):
    """Represents a link-based stack."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = None
        super().__init__(sourceCollection)

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty."""
        if self.isEmpty():
            raise ValueError("Attempt to peek at empty stack")
        
        return self._items.data

    def __iter__(self):
        """Supports iteration over a view of self, from bottom to top."""
        probe = self._items
        modCount = self.getModCount()
        while probe != None:
            yield probe.data
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed in a for loop")
            probe = probe.next

    # Mutator methods
    
    def clear(self):
        """Makes self become empty."""
        self.resetSizeAndModCount()
        self._items = None        

    def push(self, item):
        """Inserts item at top of the stack."""
        self._items = Node(item, self._items)
        self._size += 1
        self.incModCount()

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise ValueError("Attempt to pop from empty stack")
        self._size -= 1
        self.incModCount()
        data = self._items.data
        self._items = self._items.next
        return data


