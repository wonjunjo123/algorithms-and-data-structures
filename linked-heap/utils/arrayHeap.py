"""
File: arrayHeap.py
YOUR NAME GOES HERE.
"""

from .arrayList import ArrayList
from .abstractHeap import AbstractHeap


class ArrayHeap(AbstractHeap):
   """An array-based implementation of a heap."""
   
   DEFAULT_SIZE = 10
   
   def __init__(self, sourceCollection = None):
      """Initialization of a heap."""
      self._heap = ArrayList()      
      super().__init__(sourceCollection)
   
   def add(self, item):
      """Adds item to the end of the array and then walks it up to the top,
         stopping when parent is less than the new item"""
         
      self._size += 1
      self._heap.append(item)
      curPos = len(self._heap) - 1
      self.decrease_key(curPos, item)
            
   def decrease_key(self, index, key):
      """Change the item at the index to the new key, which must be smaller than its original key
         Then fix the heap going upwards
      """
      data = self._heap[index]
      if key > data:
         raise Error("Can't decrease key to a larger key!")
      else:
         while index > 0:
            parent = (index - 1) // 2
            parentItem = self._heap[parent]
            if parentItem <= key:
               break
            else:
               self._heap[index] = self._heap[parent]
               self._heap[parent] = key
               index = parent
            
   def pop(self):
      """Swaps the top element with the last element, then walks the top
         element down until both children are larger than the current node."""
      if self.isEmpty():
         raise KeyError("The heap is empty.")
         
      self._size -= 1
      topItem = self._heap[0]
      bottomItem = self._heap.pop(len(self._heap) - 1)
      
      if len(self._heap) == 0:
         return bottomItem
             
      self._heap[0] = bottomItem
      lastIndex = len(self._heap) - 1
      curPos = 0
   
      while True:
         leftChild = curPos * 2 + 1
         rightChild = curPos * 2 + 2
         
         if leftChild > lastIndex:
            break
         
         if rightChild > lastIndex:
            maxChild = leftChild
            
         else:
            leftItem  = self._heap[leftChild]
            rightItem = self._heap[rightChild]
            if leftItem < rightItem:
               maxChild = leftChild
               
            else:
               maxChild = rightChild
               
         maxItem = self._heap[maxChild]
         
         if bottomItem <= maxItem:
            break
         
         else:
            self._heap[curPos] = self._heap[maxChild]
            self._heap[maxChild] = bottomItem
            curPos = maxChild
            
      return topItem
   
   
   def __str__(self):
      """Returns a string representation with the tree rotated
         90 degrees counterclockwise."""
      def recurse(index, level):
         s = ""
         if index < len(self):
            s += recurse(index * 2 + 2, level + 1)
            s += "| " * level
            s += str(self._heap[index]) + "\n"
            s += recurse(index * 2 + 1, level + 1)
         return s
      return recurse(0, 0)
   



