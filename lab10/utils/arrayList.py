"""
File: arrayList.py
Author: YOUR NAME GOES HERE
"""

from .arrays import Array
from .abstractList import AbstractList

class ArrayList(AbstractList):
    """Represents an array-based list."""

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)

    # Accessor methods
    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError if i is out of range."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._items[i]

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        modCount = self.getModCount()
        while cursor < len(self):
            yield self._items[cursor]
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed in a for loop")
            cursor += 1

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.resetSizeAndModCount()
        self._items = Array(ArrayList.DEFAULT_CAPACITY)

    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError if i is out of range."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self._items[i] = item

    def _resize(self):
        """Private helper method to resize the array if necessary."""
        temp = None
        if len(self) == len(self._items):
            temp = Array(2 * len(self._items))
        elif len(self) <= len(self._items) // 4 and \
             len(self._items) >= 2 * ArrayList.DEFAULT_CAPACITY:
            temp = Array(len(self._items) // 2)
        if temp:
            for i in range(len(self)):
                temp[i] = self._items[i]
            self._items = temp

    def insert(self, i, item):
        """Inserts the item at position i."""
        self._resize()
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        if i < len(self):
            for j in range(len(self), i, -1):
                 self._items[j] = self._items[j - 1]
        self._items[i] = item
        self._size += 1
        self.incModCount()

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self)
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError if i is out of range."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        item = self._items[i]
        for j in range(i, len(self) - 1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        self._resize()
        self.incModCount()
        return item
    
    

    def listIterator(self):
        return ArrayList.ListIterator(self)
    

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
            return self._backingStore[self._lastItemPos]
           
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
            return self._backingStore[self._lastItemPos]

        def replace(self, item):
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Replaces the items at the current position with item."""
            if self._lastItemPos == -1:
                raise AttributeError("The current position is undefined.")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            self._backingStore[self._lastItemPos] = item
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

