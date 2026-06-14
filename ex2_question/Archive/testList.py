from linkedArrayList import linkedArrayList

def testArrayCount():
    a = linkedArrayList([x for x in range(21)])
    print("Expect 5:", a.arrayCount())
    for x in range(10):
        a.add(x)
    print("Expect 7:", a.arrayCount())
    
def testIteration():
    a = linkedArrayList([x for x in range(21)])
    print("Expect items 0 through 20 on one line")
    for item in a:
        print(item, end = " ")
    print()

def testContains():
    b = linkedArrayList([x for x in range(21)])
    print("Should be True:", 5 in b)
    print("Should be False:", 24 in b)

def testGetSet():
    c = linkedArrayList([y for y in range(30)])
    c[16] = -23
    print("Expect -23:", c[16])
    
    errors = 0
    try:
        c[31415] = 12
    except IndexError as err:
        errors +=1
        print("Got an index error as expected. ", err)
    try:
        print(c[-12])
    except IndexError as err:
        errors +=1
        print("Got a second index error as expected. ", err)
        
    print(str(errors), "out of 2 expected errors occured.")
    
def main():
    testArrayCount()
    testIteration()
    testContains()
    testGetSet()

if __name__ == "__main__":
    main()
