

from .arrayBag import ArrayBag
from ..utils.abstractCollection import AbstractCollection
from .abstractSet import AbstractSet

class ArraySet(AbstractSet, ArrayBag):
   
   def __init__(self, sourceCollection = None):
      super().__init__(sourceCollection)
   
   
   def add(self, item):
      if item not in self:
         super().add(item)
         
   def __eq__(self, other):
      return super().__eq__(other)
   
   