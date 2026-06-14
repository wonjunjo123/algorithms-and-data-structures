

class AbstractSet(object):
   
   def __or__(self, other):
      
      returnSet = type(self)(self)
      
      for item in other:
         returnSet.add(item)
      
      return returnSet
   
   def __and__(self, other):
      returnSet = type(self)()
      
      
      for item in self:
         if item in other:
            returnSet.add(item)
      
      return returnSet

   def __sub__(self, other):
      returnSet = type(self)()
      
      
      for item in self:
         if item not in other:
            returnSet.add(item)
      
      return returnSet