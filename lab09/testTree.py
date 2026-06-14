from utils.linkedBst import LinkedBST


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
    


def testTree():
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
        

def testBalance():
    tree = LinkedBST()
    print("Adding D B A C F E G")
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")

    print("\nString:\n" + str(tree))    
    print("Left height, right height:", tree._root.left.getHeight(), tree._root.right.getHeight())
    print("Length:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    
    tree = LinkedBST(range(1, 15))
    print("\nAdded 1..15:\n" + str(tree))    
    print("Left height, right height:", tree._root.left.getHeight(), tree._root.right.getHeight())
    print("Length:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    
    lyst = list(range(1, 16))
    import random
    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    print("\nAdded ", lyst, "\n" + str(tree))    
    print("Left height, right height:", tree._root.left.getHeight(), tree._root.right.getHeight())
    print("Length:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())

 
def testRemove():
    print("Testing remove")
    lyst = list(range(1, 100))
    import random
    random.shuffle(lyst)
    tree = LinkedBST(lyst)
    lyst.sort()
    for i in range(50):
        tree.remove(lyst[i])
    
    print("\nAdded 100, removed 50\n" + str(tree))
    print("Left height, right height:", tree._root.left.getHeight(), tree._root.right.getHeight())
    print("Length:", len(tree))
    print("Height:", tree.height())
    print("Balanced:", tree.isBalanced())
    
    for i in lyst[0:50]:
        if i in tree:
            print("item i should not be in tree:", i)
    for i in lyst[50:100]:
        if i not in tree:
            print("item i should be in tree:", i)

            
if __name__ == "__main__":
    testTree()
    testRotate()
    testBalance()
    testRemove()
    
