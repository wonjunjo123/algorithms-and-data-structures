"""
File: listIteratorinterface.py
Author: Ken Lambert
"""

class ListIteratorInterface(object):
    """Interface for all list iterator types."""

    def first(self):
        """Returns the cursor to the beginning of the backing store."""
        pass

    def hasNext(self):
        """Returns True if the iterator has a next item or False otherwise."""
        return False
 
    def next(self):
        """Preconditions: hasNext returns True
        The list has not been modified except by this iterator's mutators.
        Returns the current item and advances the cursor to the next item."""
        return None

    def last(self):
        """Moves the cursor to the end of the backing store."""
        pass

    def hasPrevious(self):
        """Returns True if the iterator has a previous item or False otherwise."""
        return False

    def previous(self):
        """Preconditions: hasPrevious returns True
        The list has not been modified except by this iterator's mutators.
        Returns the current item and moves the cursor to the previous item."""
        return None

    def replace(self, item):
        """Preconditions: the current position is defined.
        The list has not been modified except by this iterator's mutators.
        Replaces the items at the current position with item."""
        pass
    
    def insert(self, item):         
        """Preconditions:
        The list has not been modified except by this iterator's mutators.
        Adds item to the end if the list if the current position is undefined,
        or inserts it at that position."""
        pass
    
    def remove(self):         
        """Preconditions: the current position is defined.
        The list has not been modified except by this iterator's mutators.
        Pops the item at the current position."""
        pass

