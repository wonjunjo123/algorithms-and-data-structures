"""
File: linkedpriorityqueue.py
Author: Wonjun Jo and AJ Thomas
"""

from .node import Node
from .linkedQueue import LinkedQueue

class LinkedPriorityQueue(LinkedQueue):
    """A link-based priority queue implementation."""


    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        super().__init__(sourceCollection)

    def add(self, item):
        """Adds item to its proper place in the queue."""
        
        # If it's empty or we have the worst priority in the queue, add to the end
        if self.isEmpty() or self._rear.data <= item:
            super().add(item)
            
        # If we have higher priority than the first item, add to front
        elif self._front.data > item:
            newNode = Node(item, self._front)
            self._front = newNode
            self.incModCount()
            self._size += 1
         
        # Otherwise, iterate through linked structure,
        #  stop at node previous to the node that is > priority than the new node   
        else:
            probe = self._front
            
            while probe.next.data <= item:
                probe = probe.next
            
            newNode = Node(item, probe.next)
            probe.next = newNode
            
            self.incModCount()
            self._size += 1
            
