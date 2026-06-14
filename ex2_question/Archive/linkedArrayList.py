"""
File: linkedArrayList.py

This implements a list using a fun mix of arrays and linked structures.

Fill out the appropriate methods so that it works!
"""
from arrays import Array

class listNode(object):
    '''
    This class defines each linked node in the list
    Each node contains a storage area which is defined to an Array with the default BLOCK_SIZE
    '''
    BLOCK_SIZE = 5 
    
    def __init__(self, storage=None, next=None):
        self.storage = Array(listNode.BLOCK_SIZE)
        self.next = next

class linkedArrayList(object):
    
    def __init__(self, source=None):
        '''
        Constructs a empty list with no head or tail unless given a source collection.
        The arrayCount is also 0 at the beginning.
        '''
        self._size = 0
        self._head = self._tail = None
        self._arrayCount = 0
        if source!=None:
            for item in source:
                self.add(item)
            
    def add(self, item):
        '''
        Adds an item to the list. This goes into the tail Array unless it is filled up, in which case it will create a new array
        
        TODO: Keep count of the array count!
        '''
        if self._head == None:
            self._head = self._tail = listNode()
            self._tail.storage[0] = item
            self._size+=1
            self._arrayCount += 1
        else:
            curr_len = len(self) % listNode.BLOCK_SIZE
            if curr_len == 0: # if the current tail array is filled up
                self._tail.next = listNode() # make the 'next' into a new listNode()
                self._arrayCount += 1
                self._tail = self._tail.next # Update the tail node to be the new node created
            self._tail.storage[curr_len] = item
            self._size+=1
            
    def __len__(self):
        return self._size
        
    def arrayCount(self):
        '''
        Returns the number of arrays used so far
        '''
        return self._arrayCount
        
    def __contains__(self, item):
        '''
        Returns true only if item is in the list
        '''
        for thing in self:
            if thing == item:
                return True
            
        return False
        
    def __iter__(self):
        '''
        Iterator for the list.
        This should iterate through every item starting from the first item of the head
        
        '''
        pointer = self._head
        cursor = 0
        while pointer.next != None:
            index = cursor % listNode.BLOCK_SIZE
            if cursor != 0 and index == 0: # if we come to the end of the array
                pointer = pointer.next # make pointer point to the next listNode
            yield pointer.storage[index]
            cursor += 1
        
        
    def __getitem__(self, index):
        '''
        Returns the item at the logical index of the list
        This should raise an IndexError if the index is negative or too large
        '''
        return self[index]
        
    def __setitem__(self, index, item):
        '''
        Sets the item at the logical index of the list
        This should raise an IndexError if the index is negative or too
        '''
        return self[index]

