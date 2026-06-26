"""
File: bstnode.py
Author: Liz Matthews
"""

class BSTNode(object):
    """Represents a node for a linked binary search tree."""

    def __init__(self, data, left = None, right = None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        
    
