
class BinaryTreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child

#nuemro mayor 
def findMaxRecursive(tree):

    # Base case
    if tree is None:
        return (tree)  # Mininum value

    data = tree.data
    left_max = findMaxRecursive(tree.left)
    right_max = findMaxRecursive(tree.right)

    return max([data, left_max, right_max])

#numero menor 
def findMinRecursive(tree):

    # Base case
    if tree is None:
        return float('-info')  # Mininum value

    data = tree.data
    left_min = findMinRecursive(tree.left)
    right_min = findMinRecursive(tree.right)

    return min([data, left_min, right_min])
'''
Binary Tree
 
                      1
                      |
            ----------------------
            |                     | 
            2                     3  
 
'''


childrenLeft = BinaryTreeNode(2)
childrenRight = BinaryTreeNode(3)
root = BinaryTreeNode(1, childrenLeft, childrenRight)


minData = findMinRecursive(root)
print(minData)

maxData = findMaxRecursive(root)
print(maxData)
#imprime  min
