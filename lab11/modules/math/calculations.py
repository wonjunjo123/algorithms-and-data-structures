"""
Author: Liz Matthews
"""

import math

def getDistance(coords1, coords2):
   return math.sqrt(math.pow(coords1[0] - coords2[0], 2) + math.pow(coords1[1] - coords2[1], 2))

   
   