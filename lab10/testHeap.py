"""
File: testHeap.py
Wonjun Jo and AJ Thomas
"""


from utils.linkedHeap import LinkedHeap
from utils.arrayHeap import ArrayHeap
from utils.leftistHeap import LeftistHeap
import random


def main(heapType):
   lyst = list(range(1, 31))
   random.shuffle(lyst)
   
   
   hp = heapType()
   
   print("Adding items to heap, inspect for heap-ness:")
   for item in lyst:
      print("adding", item)
      hp.add(item)
      print(hp)
      print()
   
   print("Heap size, expect 30:", len(hp))
   print("Expect items in order:", end=" ")
   while not hp.isEmpty():
      print(hp.pop(), end=" ")
   print()
   
   print("Heap size, expect 0:", len(hp))
  
def testMerge(heapType):
    lyst = list(range(1,40))
    random.shuffle(lyst)
    hp1 = heapType()
    hp2 = heapType()
    for i in range(len(lyst)):
        if i%2:
            hp1.add(lyst[i])
        else:
            hp2.add(lyst[i])
        
    print(hp1)
    print(hp2)
    
    print("Merge heaps of size: {} and {}".format(len(hp1), len(hp2)))
    hp1.merge(hp2)
    
    print(hp1)
    if checkLeft(hp1._heap):
        print("This is indeed a leftist heap, good.")
  
    print("Expect items in order:", end=" ")
    lyst2 = []
    while not hp1.isEmpty():
        i = hp1.pop()
        lyst2.append(i)
        print(i, end=" ")
    print()
    print("There were", len(lyst2), "items.")

def checkLeft(node):
    if node != None:
        if node.left==None:
            if node.right!=None:
                raise Exception("This heap is not leftist at node with value {}".format(node.data))
        else:
            if node.right!=None:
                if node.left.h < node.right.h:
                    raise Exception("This heap is not leftist at node with value {}".format(node.data))
            checkLeft(node.left)
            checkLeft(node.right)
    return True
    
def testLeftistIdeas(heapType):
    """Makes sure that the heap follows the leftist ideas"""
    
    lyst = list(range(1,40))
    random.shuffle(lyst)
    hp1 = heapType()
    for i in range(len(lyst)):
       hp1.add(lyst[i])
    print(hp1)
    
    if checkLeft(hp1._heap):
        print("This is indeed a leftist heap, good.")
    
if __name__ == '__main__':
      
   #main(ArrayHeap)
   main(LinkedHeap)
   
   #main(LeftistHeap)
   #testLeftistIdeas(LeftistHeap)
   #testMerge(LeftistHeap)
