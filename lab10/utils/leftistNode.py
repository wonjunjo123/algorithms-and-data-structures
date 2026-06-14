"""
File: LeftistNode
Author: Kefu Lu
"""

class LeftistNode(object):
    """Represents a node for a leftist"""

    def __init__(self, data, left = None, right = None, parent=None, h = 0):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.h = 0 # Recall that h is not height, it is the distance to the closest external node on the right
        
    def isExternal(self):
        return self.left == None or self.right == None
    
    def updateH(self):
        if self.isExternal():
            self.h=0
        else:
            self.h = self.right.h + 1
    
