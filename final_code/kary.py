class KAryHeap():
    """An array-based implementation of a kary heap."""   
    def __init__(self, sourceCollection = None, k = 4):
        """Initialization of a heap."""
        self._heap = []
        self._k = k
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
    
    def add(self, item):
        """Adds item to the end of the array and calls decrease_key on it,
            stopping when parent is less than the new item"""
            
        self._size += 1
        self._heap.append(item)
        curPos = len(self._heap) - 1
        self.decrease_key(curPos, item)
        
    def decrease_key(self, index, key):
        """
            Change the item at the index to the new key, which must be smaller than its original key
            Then fix the heap going upwards
        """

        self._heap[index] = key
        parentIndex = (index - 1)//self._k
        
        while self._heap[index] < self._heap[parentIndex]:
            self._heap[index], self._heap[parentIndex] = self._heap[parentIndex], self._heap[index]
            index = parentIndex
            if index == 0:
                break
            parentIndex = (index - 1)//self._k
            
        
        
                
    def pop(self):
        """Swaps the top element with the last element"""
        if self.isEmpty():
            raise KeyError("The heap is empty.")
            
        self._size -= 1
        topItem = self._heap[0]
        bottomItem = self._heap.pop(len(self._heap) - 1)
        
        if len(self._heap) == 0:
            return bottomItem
                 
        self._heap[0] = bottomItem        
        self.heapify(0)
        return topItem
        
    def heapify(self, index):
        """
        Walks the top element down until all children are larger than the current node.
        """
        
        leftmostIndex = index*self._k + 1
        rightmostIndex = index*self._k + self._k # can be factored out to (index + 1)*self._k
        
        count = 0
        minIndex = leftmostIndex # variable to keep track of index with smallest item of node's k children
        for i in range(leftmostIndex, rightmostIndex+1):
            if i >= len(self._heap) or minIndex >= len(self._heap):
                return # this is to avoid index out of bounds
            if self._heap[i] < self._heap[minIndex]: # if current item is smaller
                minIndex = i # update minIndex to be current index
            
            if self._heap[index] < self._heap[i]:
                count += 1
        if count == self._k: # if item is smaller than all of its k children, this observes heap property
            return

        # if it doesn't observe heap property then, swap with smallest value
        self._heap[index], self._heap[minIndex] = self._heap[minIndex], self._heap[index]
        self.heapify(minIndex)

        
    
    def __len__(self):
        return self._size
        
    def __str__(self):
        return str(self._heap)
        
    def isEmpty(self):
        return self._size==0
    
def main():
    import random
    x = [i for i in range(25)]
    random.shuffle(x)
    f = KAryHeap(x, k=2)
    print("There should be 25 items:", len(f))
    print("They should be in heap order:", f)
    print("Pop each item one by one!")
    while not f.isEmpty():
        print(f.pop(), end = " ")
    print()
        
    f = KAryHeap(x)
    print("There should be 25 items:", len(f))
    print("They should be in heap order:", f)
    print("Pop each item one by one!")
    while not f.isEmpty():
        print(f.pop(), end = " ")
    print()
        
if __name__ == "__main__":
    main()


