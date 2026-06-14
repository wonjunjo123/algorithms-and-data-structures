"""
File: linkedList.py
Author: Wonjun Jo and AJ Thomas
"""

from .node import TwoWayNode
from .abstractList import AbstractList

class LinkedList(AbstractList):
    """A link-based list implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Uses a circular linked structure with a dummy header node
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        super().__init__(sourceCollection)

    # Helper method returns node at position i
    def _getNode(self, i):
        """Helper method: returns a pointer to the node at position i."""
        if i == (len(self) - 1):
            return self._head.previous
        
        probe = self._head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    #Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._head.next
        modCount = self.getModCount()
        while cursor != self._head:
            yield cursor.data
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed in a for loop")
            cursor = cursor.next

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._getNode(i).data

    # Mutator methods
    def clear(self):
        self._head.previous = self._head.next = self._head
        self.resetSizeAndModCount()
    
    def __setitem__(self, i, item):
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self._getNode(i).data = item
    
    def insert(self, i, item):
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        
        probe = self._getNode(i)
        newNode = TwoWayNode(item, probe.previous, probe)
        probe.previous.next = newNode
        probe.previous = newNode
        
        self._size += 1
        self.incModCount()
        
    
    def pop(self, i = None):
        """Precondition: 0 <= i < len(self)
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError if i is out of range."""
        if i == None:
            i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError('i is out of range')

        probe = self._getNode(i)
        item = probe.data
        probe.previous.next = probe.next
        probe.next.previous = probe.previous

        self._size -= 1
        self.incModCount()
        
        
        return item
        
    
    def listIterator(self):
        return LinkedList.ListIterator(self)
        
        
        
    
    # Use _getNode wherever possible to support access to the ith node
    class ListIterator(object):
        """Represents a list iterator."""

        def __init__(self, backingStore):
            """Sets the initial state of the list iterator."""
            self._backingStore = backingStore
            self._modCount = backingStore.getModCount()
            self.first()

        def first(self):
            """Returns the cursor to the beginning of the backing store.
            lastItemPos is undefined."""
            self._cursor = 0
            self._lastItemPos = -1

        def hasNext(self):
            """Returns True if the iterator has a next item or False otherwise."""
            return self._cursor < len(self._backingStore)

        def next(self):
            """Preconditions: hasNext returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and advances the cursor to the next item.
            Postcondition: lastItemPos is now defined.
            Raises: ValueError if no next item.
            AttributeError if illegal mutation of backing store."""
            if not self.hasNext():
                raise ValueError("No next item in list iterator")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("Illegal modification of backing store")
            self._lastItemPos = self._cursor
            self._cursor += 1

            probe = self._backingStore._head.next
            i = self._lastItemPos
            while i > 0:
                probe = probe.next
                i -= 1

            return probe.data
            #return self._backingStore._getNode(self._lastItemPos).data
           
        def last(self):
            """Moves the cursor to the end of the backing store."""
            self._cursor = len(self._backingStore)
            self._lastItemPos = -1

        def hasPrevious(self):
            """Returns True if the iterator has a previous item or False otherwise."""
            return self._cursor > 0

        def previous(self):
            """Preconditions: hasPrevious returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and moves the cursor to the previous item."""
            if not self.hasPrevious():
                raise ValueError("No previous item in list iterator")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("Illegal modification of backing store")
            self._cursor -= 1
            self._lastItemPos = self._cursor
            
            probe = self._backingStore._head.next
            i = self._lastItemPos
            while i > 0:
                probe = probe.next
                i -= 1

            return probe.data
        

        def replace(self, item):
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Replaces the items at the current position with item."""
            if self._lastItemPos == -1:
                raise AttributeError("The current position is undefined.")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")

            probe = self._backingStore._head.next
            i = self._lastItemPos
            while i > 0:
                probe = probe.next
                i -= 1
            newNode = TwoWayNode(item, probe.previous, probe.next)
            probe.next.previous = newNode
            probe.previous.next = newNode
            self._lastItemPos = -1


        def insert(self, item):         
            """Preconditions:
            The list has not been modified except by this iterator's mutators.
            Adds item to the end if the current position is undefined, or
            inserts it at that position."""
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            if self._lastItemPos == -1:
                self._backingStore.add(item)
            else:
                self._backingStore.insert(self._lastItemPos, item)
                self._lastItemPos = -1
            self._modCount += 1

        def remove(self):         
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Pops the item at the current position."""
            if self._lastItemPos == -1:
                raise AttributeError("The current position is undefined.")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            item = self._backingStore.pop(self._lastItemPos)
            # If the item removed was obtained via next, move cursor back
            if self._lastItemPos < self._cursor:
                self._cursor -= 1
            self._modCount += 1
            self._lastItemPos = -1













