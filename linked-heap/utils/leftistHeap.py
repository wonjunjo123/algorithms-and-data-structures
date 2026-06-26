"""
File: leftistHeap.py
Wonjun Jo and AJ Thomas
"""


from .abstractHeap import AbstractHeap
from .leftistNode import LeftistNode
import math


class LeftistHeap(AbstractHeap):
    """A leftist implementation of a heap."""

    def __init__(self, sourceCollection = None):
      """Initialization of a heap."""
      self._heap = None
      super().__init__(sourceCollection)


    def add(self, item):
        """
        Adds the item to the heap
        
        """
        if self._heap == None:
            self._heap = LeftistNode(item)
        else:
            self._heap = self.node_merge(self._heap, LeftistNode(item))
            
        self._size += 1
      
    def pop(self):
        """Pops the top item and then fixes the heap by merging"""
        #You should add code here

        if self._heap == None: # or len(self) == 0
            raise KeyError('Heap is empty')
        
        elif len(self) == 1:
            value = self._heap.data
            self._heap = None
            
        else:
            value = self._heap.data
            self._heap = self.node_merge(self._heap.left, self._heap.right)
            
        self._size -= 1
        
        return value
    
    def merge(self, other):
        """
        Merges self with the other heap
        Set self's _heap to be the new root after the merge
        """
        self._heap = self.node_merge(self._heap, other._heap)
        self._size += len(other)
        
    def node_merge(self, nodeA, nodeB):
        """
        Merges the two leftist heaps rooted at two nodes, A, and B
        Returns the new root
        """

        if not nodeA:
            return nodeB
        elif not nodeB:
            return nodeA
        
        if nodeA.data <= nodeB.data:
            smallerNode = nodeA
            biggerNode = nodeB
        else:
            smallerNode = nodeB
            biggerNode = nodeA

        # if both heaps have only 1 node
        if smallerNode.left == None and smallerNode.right == None and biggerNode.left == None and biggerNode.right == None:
               smallerNode.left = biggerNode # just a simple heap
               return smallerNode
        else:

            # recursively merging
            smallerNode.right = self.node_merge(smallerNode.right, biggerNode)

            # if heap is not leftist at any given point, swap right and left
            if (smallerNode.right and not smallerNode.left) or smallerNode.right.h > smallerNode.left.h:
                smallerNode.right, smallerNode.left = smallerNode.left, smallerNode.right

        smallerNode.updateH()

        return smallerNode
    
        
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self._heap, 0)









    

