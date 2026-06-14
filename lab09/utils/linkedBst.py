"""
File: linkedBst.py
Author: Wonjun Jo and AJ Thomas
"""

from .abstractCollection import AbstractCollection
from .bstNode import BSTNode
from math import log
from .linkedStack import LinkedStack
from .linkedQueue import LinkedQueue

class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        super().__init__(sourceCollection)
        
    # Accessor methods
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
        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        
        return self.preorder()
    
    def height(self):
        if self._root == None:
            return 0
        return self._root.getHeight()
    
    def isBalanced(self):
        if self._root == None:
            return True
        return self._root.isBalanced()

    def preorder(self):
        """Supports an preorder traversal on a view of self."""
        q = LinkedStack()
        myModCount = self.getModCount()
        
        q.add(self._root)
        
        while not q.isEmpty():
            item = q.pop()
            
            yield item.data

            if item.right:
                q.add(item.right)
            if item.left:
                q.add(item.left)
            

    def inorder(self):
        """Supports an inorder traversal on a view of self."""

        stack = LinkedStack()
        probe = self._root
        while True:
            if probe:
                stack.add(probe)
                probe = probe.left
            elif not stack.isEmpty():
                probe = stack.pop()
                yield probe.data
                probe = probe.right
            else:
                break

    def postorder(self):
        """Supports an postorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self._root)
        for item in lyst:
            yield item
            
        
    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        q = LinkedQueue()
        myModCount = self.getModCount()
        
        
        q.add(self._root)
        
        while not q.isEmpty():
            item = q.pop()
            
            yield item.data
            
            if item.left:
                q.add(item.left)
            if item.right:
                q.add(item.right)
        
        
    
    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        def recurse(node):
            if node is None:
                return None
            elif  item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
            
        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self.resetSizeAndModCount()

    def add(self, item):
        """Adds item to the tree."""

        # Recursive definition
        def recurse(node):
            # If we run off the end of the tree this is where the item goes
            if not node:
                return BSTNode(item)
            
            # Traverse left
            elif item < node.data:                
                node.left = recurse(node.left)
                
            # Traverse right
            else:
                node.right = recurse(node.right)
                
            # Update height and get balance
            node.updateHeight()            
            balance = node.getBalance()
            
            # AVL rebalance here
            # Check if the tree is balanced at the node, if not, do some rotations.
            # Draw out the imbalance if you need to visualize it!
            if balance > 1: # if tree is imbalanced and it went in the left
                leftBalance = node.left.getBalance()
                
                if leftBalance > 0: # if item went into left of the left
                    node = self._rightRotate(node)

                    
                elif leftBalance < 0: # if item went into right of the left
                    node.left = self._leftRotate(node.left)
                    node = self._rightRotate(node)


                    
            elif balance < -1: # if tree is imbalanced and it went in the right
                rightBalance = node.right.getBalance()
                
                if rightBalance < 0: # if item went into right of the right
                    node = self._leftRotate(node)

                    
                elif rightBalance > 0: # if item went into left of the right
                    node.right = self._rightRotate(node.right)
                    node = self._leftRotate(node)

            
            
            return node
            

        
        self._root = recurse(self._root)
        self._size += 1
        self.incModCount()

    

        
    
    #Make sure we are rotating properly!
    #These method should do a rotation ROOTED at the node
    #Return the node that is the new root after the rotation
        
    def _leftRotate(self, node):

        temp = None
        
        if node.right.left:
            temp = node.right.left
        node.right.left = node
        newroot = node.right
        node.right = temp

        node.updateHeight()
        newroot.updateHeight()
        return newroot
  
    def _rightRotate(self, node):  
         
        temp = None
        
        if node.left.right:
            temp = node.left.right
        node.left.right = node
        newroot = node.left
        node.left = temp
        
        node.updateHeight()
        newroot.updateHeight()
        return newroot
    
    

    def remove(self, item):
        
        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            
            # Keep track of the parent and the current node, start by going left once
            parent = top
            currentNode = top.left
            
            # Go right until we can't anymore
            while currentNode.right:
                parent = currentNode
                currentNode = currentNode.right
            
            # Update the top's data to be the max from the left subtree
            top.data = currentNode.data
            
            # Remove moved data from the subtree
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left
        
        def recurse(node):
            
            if not node:
                raise KeyError('item not in tree')

            elif item == node.data:
                    
                if not node.left: # because node.left is a precondition to liftMax
                    return node.right
                else:
                    liftMaxInLeftSubtreeToTop(node)

            # Traverse left
            elif item < node.data:     
                node.left = recurse(node.left)
                
            # Traverse right
            else:
                node.right = recurse(node.right)
                
            # Update height and get balance
            node.updateHeight()            
            
            return node
        
        
        self._root = recurse(self._root)
        self._size -= 1
        self.incModCount()
        
        return item
                

    def replace(self, item, newItem):
        """Precondition: item == newItem.
        Raises: KeyError if item != newItem.
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        if item != newItem: raise KeyError("Items must be equal")
        probe = self._root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None
    

def testRotate():
    t = LinkedBST("D B A C F E G".split())
    print("Normal tree:")
    print(t)
    
    t._root.right = t._leftRotate(t._root.right)
    
    print("Rotated left from node F:")
    print(t)
    
    t._root.right = t._rightRotate(t._root.right)
    
    print("Rotated right from node G:")
    print(t)
    
    t._root.right = t._rightRotate(t._root.right)
    
    print("Rotated right from node F:")
    print(t)
    


def main():
    print("Adding A B C D E F G")
    skinny = LinkedBST("A B C D E F G".split())

    print("\nString for skinny tree:\n" + str(skinny))

    print("Adding D B A C F E G")
    bushy = LinkedBST("D B A C F E G".split())

    print("\nString for bushy tree:\n" + str(bushy))

    print("\nExpect True for A in bushy tree: ", "A" in bushy)

    clone = LinkedBST(bushy)
    print("\nClone of bushy tree:\n" + str(clone))
    
    print("Expect True for bushy tree == clone: ", bushy == clone)

    print("\nFor loop: ", end="")
    for item in bushy:
        print(item, end=" ")

    print("\n\ninorder traversal, expect A B C D E F G: ", end="")
    for item in bushy.inorder(): print(item, end = " ")
    
    print("\n\npreorder traversal, expect D B A C F E G: ", end="")
    for item in bushy.preorder(): print(item, end = " ")
    
    print("\n\npostorder traversal, expect A C B E G F D: ", end="")
    for item in bushy.postorder(): print(item, end = " ")
    
    print("\n\nlevelorder traversal, expect D B F A C E G: ", end="")
    for item in bushy.levelorder(): print(item, end = " ")

    print("\n\nRemoving all items:", end = " ")
    for item in "ABCDEFG":
        print(bushy.remove(item), end=" ")

    print("\n\nExpect 0: ", len(bushy))

    tree = LinkedBST(range(1, 16))
    print("\nAdded 1..15:\n" + str(tree))
    
    lyst = list(range(1, 16))
    import random
    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print("\nAdded ", lyst, "\n" + str(tree))

    tree = LinkedBST(list("DBACFEG"))
    print("Added " + str(list("DBACFEG")))
    print(tree)
    print("Expect exception, trying to mutate in a for loop")
    try:
        count = 1
        for item in tree:
            tree.add(item + str(count))
            count += 1
    except Exception as e:
        print("Exception happened, '" + str(e) + "'")
    
if __name__ == "__main__":
    main()


