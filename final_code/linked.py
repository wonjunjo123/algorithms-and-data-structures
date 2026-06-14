


class LinkedNode():
    def __init__(self, data, n=None):
        self._data = data
        self._next = n
        
    def __le__(self, other):
        if other == None:
            return False
        if type(self)!=type(other): 
            return False
        return self._data <= other._data
    
class SLList():        
    ''' A sorted linked list '''
    def __init__(self, sourceCollection = None, k = 4):
        """
        Initialization of a list
        The head and tail point to the start and end of the list respectively
        """
        self._head = self._tail = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                
    def add(self, item):
        if len(self)==0:
            self._head = self._tail = LinkedNode(item, self._head)
        elif item < self._head._data:
            self._head = LinkedNode(item, self._head)
        elif item > self._tail._data:
            self._tail._next = LinkedNode(item)
            self._tail = self._tail._next
        else:
            t = p = self._head
            while p:
                if p._data > item:
                    break
                else:
                    t = p
                    p = p._next
            t._next = LinkedNode(item, p)
        self._size+=1
        
    def __len__(self):
        return self._size
        
    def __str__(self):
        res = ''
        p = self._head
        while p:
            res += str(p._data) + " "
            p=p._next
        return res
        
    def isEmpty(self):
        return self._size==0

def destructive_merge(A, B):
    '''
    Returns a List which contains all the items from A and B in order
    For full credit, this should not create any new nodes but can destroy A and B instead
    (By changing the references of their nodes)
    (E.g. splice together the lists)
    '''
    
    if A._head._data < B._head._data:
        return_heap = A # the heap we are going to return
        destroy_heap = B # the heap we are going to take from and redirect into A

    else:
        return_heap = B
        destroy_heap = A

    # update tail
    if A._tail._data > B._tail._data:
        return_heap._tail = A._tail
    else:
        return_heap._tail = B._tail

    # update size
    return_heap._size += destroy_heap._size

    probe1 = return_heap._head
    probe2 = destroy_heap._head
    

    
    while probe1:
        while probe1._next and probe2 and probe2._data < probe1._next._data:
            temp = probe2._next 
            probe2._next = probe1._next
            probe1._next = probe2
            probe2 = temp
            probe1 = probe1._next
            if probe2 == None: # when everything from destroy_heap has been redirected to return_heap
                return return_heap

        probe1 = probe1._next

        
    return return_heap
    
    
def main():
    import random
    x = [random.randint(0, 50) for i in range(10)]
    y = [random.randint(0, 50) for i in range(10)]
    fx = SLList(x)
    fy = SLList(y)
    
    print("There should be 10 items:", len(fx))
    print("They should be in order:", fx)
    print("There should be 10 items:", len(fy))
    print("They should be in order:", fy)
    
    c = destructive_merge(fx, fy)
    print("There should be 20 items:", len(c))
    print("They should be in order:", c)
    print("The head is: ", c._head._data)
    print("The tail is: ", c._tail._data)
    
        
if __name__ == "__main__":
    main()
