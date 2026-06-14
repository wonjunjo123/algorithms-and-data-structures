INFINITY = "-"



def addWithInfinity(a, b):
   """Adds a and b, with the possibility that either might be infinity."""
   if a == INFINITY or b == INFINITY:
      return INFINITY
   else:
      return a + b
    
def minWithInfinity(a, b):
   """Finds the minimum of a and b, with the possibility that either might be infinity."""
   if a == INFINITY:
      return b
   elif b == INFINITY:
      return a
   else:
      return min(int(a), int(b))
    

def lessThanWithInfinity(a, b):
   """Returns a < b, with the possibility that either might be infinity."""
   if a == INFINITY:
      return False
   elif b == INFINITY:
      return True
   else:
      return a < b
   