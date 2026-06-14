
"""
File: testList.py
Author: Wonjun Jo and AJ Thomas
"""

from utils.arrayList import ArrayList
from utils.linkedList import LinkedList

def testList(listType):
    lyst = listType()
    print('{0}TESTING {1}{0}'.format('-'*18, str(listType)))
    print()

    print('Creating new empty list...')
    print('Testing: isEmpty')
    print('Test if empty, expect True: {}'.format(lyst.isEmpty()))
    print()

    print('Testing: add / __str__')
    print('Adding integers 0 to 9 inclusive to list')
    for x in range(10):
        lyst.add(x)
    print('Test string representation, expect [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:\n{}'\
          .format(lyst))
    print()

    print('Testing: __len__')    
    print('Test if length is 10, expect 10: {}'.format(len(lyst)))
    print('Test if empty, expect False: {}'.format(lyst.isEmpty()))
    print()
    
    print('Testing: __iter__')
    print('Print each item in list vertically:')
    for item in lyst:
        print(item)
    print('Attempt modifications within loop')
    try:
        for item in lyst:
            lyst.append(item)
    except Exception as e:
        print('Successfully Crashed: {}'.format(e))
    print()
    
    print('Testing: __add__')
    print('Adding lyst2 = [10, 11, 12, 13, 14] to lyst (lyst + lyst2)')
    lyst = listType([0,1,2,3,4,5,6,7,8,9])
    lyst2 = listType([10,11,12,13,14])
    lyst3 = lyst + lyst2
    print('Expect list to be all integers from 0 to 14 inclusive:')
    print(lyst3)
    print()

    print('Testing: __eq__')
    print('Making a copy of list and seeing if they are equal:')
    copy = listType(lyst)
    print('lyst = {} // copy = {}'.format(lyst, copy))
    print('lyst == copy, expect True: {}'.format(copy == lyst))
    print('Clearing copy...')
    copy.clear()
    print('Copy is cleared and should be empty, expect True: {}'.format(copy.isEmpty()))
    print()

    print('Testing: __getitem__')
    print('Let lyst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]')
    lyst = listType([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    print('lyst[0], expect 0: {}'.format(lyst[0]))
    print('lyst[len(lyst)-1], expect 14: {}'.format(lyst[len(lyst)-1]))
    print('lyst[4], expect 4: {}'.format(lyst[4]))
    try:
        print(lyst[10000])
    except Exception as e:
        print('lyst[10000] -> Successfully Crashed: {}'.format(e))
    try:
        print(lyst[-5])
    except Exception as e:
        print('lyst[-5] -> Successfully Crashed: {}'.format(e))
    print()
    
    print('Testing: count')
    print('Let lyst = [0,1,2,2,2,4,4,6]')
    lyst = listType([0,1,2,2,2,4,4,6])
    print('2 occurs 3 times in the list, expect 3: {}'.format(lyst.count(2)))
    print('6 occurs 1 time in the list, expect 1: {}'.format(lyst.count(6)))
    print('7 occurs 0 times in the list, expect 0: {}'.format(lyst.count(7)))
    print()

    print('Testing: index')
    print('Let lyst = [0,1,2,2,2,4,4,6]')
    print('Index of 1, expect 1: {}'.format(lyst.index(1)))
    print('Index of 4, expect 5: {}'.format(lyst.index(4)))
    print('Index of 6, expect 7: {}'.format(lyst.index(6)))
    try:
        print(lyst.index(7))
    except Exception as e:
        print('Index of 7, lyst.index(7) -> Successfully Crashed: {}'.format(e))
    print()

    print('Testing: clear')
    lyst.clear()
    print('Lyst should have nothing in it, expect []: {}'.format(lyst))
    print('Lyst should be empty, expect True: {}'.format(lyst.isEmpty()))
    print()

    print('Testing: append')
    print('Appending numbers...')
    for x in range(10):
        lyst.append(x)
        if x%2 == 1: # if number is odd, add twice... this is just to add variety to the list
            lyst.append(x)
    print('List should be [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]: \n{}'\
          .format(lyst))
    print()

    print('Testing: remove')
    print('Start with previous list: {}'.format(lyst))
    lyst.remove(0)
    lyst.remove(2)
    lyst.remove(4)
    print('Remove 0, 2, and 4: {}'.format(lyst))
    lyst.remove(6)
    lyst.remove(8)
    lyst.remove(9)
    print("Remove 6, 8, and one of the 9's: {}".format(lyst))
    lyst.remove(5)
    lyst.remove(5)
    lyst.remove(9)
    print("Remove both 5's and the other 9: {}".format(lyst))
    try:
        lyst.remove(10)
    except Exception as e:
        print('Attempt to remove 10 from list -> Successfully Crashed: {}'\
              .format(e))
    print()
    
    print('Testing: insert')
    lyst = listType([1,4,7,10])
    print('Let lyst = [1, 4, 7, 10]')
    lyst.insert(2, 5)
    print('Insert 5 at index 2, expect [1, 4, 5, 7, 10]: \n{}'.format(lyst))
    lyst.insert(len(lyst) - 1, 9)
    print('Insert 9 at final index, expect [1, 4, 5, 7, 9, 10]: \n{}'.format(lyst))
    lyst.insert(0, 0)
    print('Insert 0 at front, expect [0, 1, 4, 5, 7, 9, 10]: \n{}'.format(lyst))
    lyst.insert(len(lyst), 13)
    print('Insert 13 at end, expect [0, 1, 4, 5, 7, 9, 10, 13]: \n{}'.format(lyst))
    lyst.insert(len(lyst) + 10, 15)
    print('Insert 15 at end (by inputting upper out of bounds index)\nexpect [0, 1, 4, 5, 7, 9, 10, 13, 15]: \n{}'.format(lyst))
    lyst.insert(-10, -3)
    print('Insert -3 at front (by inputting lower out of bounds index)\nexpect [-3, 0, 1, 4, 5, 7, 9, 10, 13, 15]: \n{}'.format(lyst))
    print()
    
    print('Testing: pop')
    lyst = listType([1,2,3,4,5])
    print('Let lyst = [1, 2, 3, 4, 5]')
    print('Pop last item on list, expect to return 5: {}'.format(lyst.pop()))
    print('List should be [1, 2, 3, 4]: {}'.format(lyst))
    print('Pop first item on list, expect to return 1: {}'.format(lyst.pop(0)))
    print('List should be [2, 3, 4]: {}'.format(lyst))
    print('Pop item at index 1, expect to return 3: {}'.format(lyst.pop(1)))
    print('List should be [2, 4]: {}'.format(lyst))
    try:
        lyst.pop(-2)
    except Exception as e:
        print('Attempt to pop index -2 -> Successfully Crashed: {}'.format(e))
    try:
        lyst.pop(len(lyst) + 3)
    except Exception as e:
        print('Attempt to pop index len(lyst) + 3 -> Successfully Crashed: {}'.format(e))
    print()

    print('Testing: __setitem__')
    lyst = listType([1,2,3,4,5])
    print('Let lyst = [1, 2, 3, 4, 5]')
    lyst[1] = 6
    print('Set lyst[1] to 6, expect [1, 6, 3, 4, 5]: {}'.format(lyst))
    lyst[0] = 9
    print('Set lyst[0] to 9, expect [9, 6, 3, 4, 5]: {}'.format(lyst))
    lyst[len(lyst) - 1] = 8
    print('Set lyst[len(lyst) - 1] to 8, expect [9, 6, 3, 4, 8]: {}'.format(lyst))
    try:
        lyst[-2] = 0
    except Exception as e:
        print('Attempt to set item in index -2 -> Successfully Crashed: {}'.format(e))
    try:
        lyst[len(lyst) + 2] = 10
    except Exception as e:
        print('Attempt to set item in index len(lyst) + 2 -> Successfully Crashed: {}'.format(e))
    print()

    
    print('Testing: slice')
    print('Let lyst = [1, 2, 3, 4, 5]')
    lyst = ArrayList([1,2,3,4,5])
    print('lyst[1:3], expect [2, 3]: {}'.format(lyst[1:3]))
    print('lyst[:3], expect [1, 2, 3]: {}'.format(lyst[:3]))
    print()

def testListIterator(listType):

    print('{0}TESTING iterator for {1}{0}'.format('-'*15, str(listType)))
    print()
    
    print('Creating iterator...')
    lyst = listType([1,2,3,4,5])
    iterator = listType.ListIterator(lyst)
    backingStore = iterator._backingStore
    print('BackStore should be [1, 2, 3, 4, 5]: {}'.format(backingStore))
    print()

    print('Testing: first')
    print('Currently: cursor = {}, lastItemPos = {}'.format(iterator._cursor, iterator._lastItemPos))
    print('Modifying cursor and lastItemPos...')
    iterator._cursor += 4
    iterator._lastItemPos += 4
    print('Modified: cursor = {}, lastItemPos = {}'.format(iterator._cursor, iterator._lastItemPos))
    print('Applying the first function...')
    iterator.first()
    print('Reset: cursor = {}, lastItemPos = {}'.format(iterator._cursor, iterator._lastItemPos))
    print()

    print('Testing: hasNext')
    print('Should print True the number of items there are (5 times) and then one False to indicate iterator has no next')
    while iterator._cursor <= len(backingStore):
        print(iterator.hasNext())
        iterator._cursor += 1
    iterator.first()
    print()
    
    print('Testing: next')
    print('Should print 1 to 5 vertically and then crash')
    try:
        for x in range(len(backingStore)+1):
            print(iterator.next())
    except Exception as e:
        print('Successfully Crashed -> {}'.format(e))
    iterator.first()
    print()
    
    print('Testing: last')
    print('Currently: cursor = {}, lastItemPos = {}'.format(iterator._cursor, iterator._lastItemPos))
    print('Applying the last function...')
    print('cursor should now be {} and lastItemPos should now be -1'.format(len(backingStore)))
    iterator.last()
    print('Now: cursor = {}, lastItemPos = {}'.format(iterator._cursor, iterator._lastItemPos))
    print()

    print('Testing: hasPrevious')
    print('Start with cursor = {}, lastItemPos = {}'.format(iterator._cursor, iterator._lastItemPos))
    print('Now applying the first function...')
    iterator.first()
    print('Iterator is reset to first, iterator has no previous, expect False: {}'.format(iterator.hasPrevious()))
    print()    

    print('Testing: previous')
    print('Placing cursor at last...')
    iterator.last()
    print('Should print 5 to 1 vertically and then crash')
    try:
        for x in range(len(backingStore)+1):
            print(iterator.previous())
    except Exception as e:
        print('Successfully Crashed -> {}'.format(e))
    iterator.first()
    print()

    print('Testing: replace')
    print('Current backingStore: {}'.format(backingStore))
    print('Replacing each item with its double...')
    for x in range(len(backingStore)):
        a = iterator.next()
        iterator.replace(2*a)
    print('Modified backingStore: {}'.format(backingStore))
    print('Applying first function and call replace, should crash...')
    iterator.first()
    try:
        iterator.replace(0)
    except Exception as e:
        print('Successfully Crashed -> {}'.format(e))
    print()
    
    print('Testing: insert')
    print('Current backingStore: {}'.format(backingStore))
    print('Inserting 0 at front...')
    iterator.next()
    iterator.insert(0)
    print('Modified backingStore: {}'.format(backingStore))
    print('Inserting 0 at end...')
    iterator.last()
    iterator.insert(0)
    print('Modified backingStore: {}'.format(backingStore))
    print()
    
    print('Testing: remove')
    print('Current backingStore: {}'.format(backingStore))
    print('Removing 0 at front...')
    iterator.first()
    iterator.next()
    iterator.remove()
    print('Modified backingStore: {}'.format(backingStore))
    print('Removing 0 at end...')
    iterator.last()
    iterator.previous()
    iterator.remove()
    print('Modified backingStore: {}'.format(backingStore))
    print()


if __name__ == '__main__':
    testList(ArrayList)
    #testList(LinkedList)
    #testListIterator(ArrayList)
    #testListIterator(LinkedList)








