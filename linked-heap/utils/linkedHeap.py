"""
File: linkedHeap.py
Wonjun Jo and AJ Thomas
"""


from .abstractHeap import AbstractHeap
from .bstNode import BSTNode
import math


class LinkedHeap(AbstractHeap):
   """A link-based implementation of a heap."""
   
   def __init__(self, sourceCollection = None):
      """Initialization of a heap."""
      self._heap = None
      super().__init__(sourceCollection)
      
   def add(self, item):
      """Adds item to the end and then walks it upwards."""
      self._size += 1
      path = self._findPathToLastNode()

      if len(self) == 1:
         self._heap = BSTNode(item)
      else:
         probe = self._heap
         for index in range(len(path)):
            direction = path[index]
            if index == len(path) - 1:
               if direction == 'left':
                  probe.left = BSTNode(item)
                  probe.left.parent = probe
                  self._walkUp(probe.left)
               elif direction == 'right':
                  probe.right = BSTNode(item)
                  probe.right.parent = probe
                  self._walkUp(probe.right)
               
            else:
               if direction == 'left':
                  probe = probe.left
               elif direction == 'right':
                  probe = probe.right
                          
      
   def pop(self):
      """Swaps the top element with the last element, then walks the top downwards."""
      if self.isEmpty():
         raise KeyError("The heap is empty.")
      elif len(self) == 1: # if there is only one value, then just remove and return value
         value = self._heap.data
         self._heap = None
      else:
         path = self._findPathToLastNode()

         # Now go to the last added node
         probe = self._heap
         for index in range(len(path)):
            direction = path[index]
            if direction == 'left':
               probe = probe.left
            elif direction == 'right':
               probe = probe.right

         # Don't need to swap because we are just going to remove the other value
         # Just need to put probe.data into self._heap.data
         value = self._heap.data # return this at the end
         self._heap.data = probe.data

         # Now just remove the last added node
         if path[-1] == 'left':
            probe.parent.left = None
         elif path[-1] == 'right':
            probe.parent.right = None

         # Heapify
         self._walkDown(self._heap)

      self._size -= 1
      return value
         
         
     
   def _walkUp(self, node):
      """Walks node's data upwards through its parents while
         it is smaller than the parent."""
      
      while node.parent and node.data < node.parent.data:
         temp = node.data
         node.data = node.parent.data
         node.parent.data = temp
         node = node.parent
      
         
   def _walkDown(self, node):
      """Walks node's data downwards through its children while
         it is larger than a child.
         I.e. heapify
      """
      probe = node
      left = probe.left
      right = probe.right
      
      if left and right: # if both left and right exist
         minimum = min(left.data, right.data)
      elif left: # if only left exists
         minimum = left.data
      elif right: # if only right exists
         minimum = right.data
      else: # has no children
         return

      
      if probe.data < minimum: # if data is smaller than both children
         return # don't do anything
      else:
         if minimum == left.data: # if left is smaller or left == right
            temp = probe.data
            probe.data = left.data
            left.data = temp
            self._walkDown(left)
         elif minimum == right.data: # if right is smaller
            temp = probe.data
            probe.data = right.data
            right.data = temp
            self._walkDown(right)
      


   

   def _findPathToLastNode(self):
      """Calculates the path to the last node in a linked
         heap based on the total number of items stored."""
      
      n = len(self)
      path = []
      
      total = math.floor(math.log(n, 2)) + 1
      
      for i in range(total - 2, -1, -1):
         if (n // math.pow(2, i)) % 2 == 0:
            path.append("left")
         else:
            path.append("right")
      
      # Return list of directions
      return path

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
