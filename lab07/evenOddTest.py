

from utils.comparable import EvenThenOdd
from utils.linkedPriorityQueue import LinkedPriorityQueue

def main():
   q = LinkedPriorityQueue()
   
   for i in range(10):
      q.add(EvenThenOdd(i))
   
   print(q)

if __name__ == '__main__':
   main()