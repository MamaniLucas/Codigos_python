# 🡺  D.L.R.

class BinaryTreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child

# Pre-order recursivc traversal.
# The nodes' values are appended to
# the result list in traversal order


def preOrderRecursive(root, result):

    if not root:
        return

    result.append(root.data)
    preOrderRecursive(root.left, result)
    preOrderRecursive(root.right, result)

'''
Binary Tree : Preorder Traversal
 
                      1
                      |
            ----------------------
            |                     | 
            2                     3  
            |                     | 
       ----------            ------------          
       |        |            |          |
       4        5            6          7
 
     --> 1 2 4 5 3 6 7
'''

childrenLeft = BinaryTreeNode("2")
childrenRight = BinaryTreeNode("3")
# los nodos nuevos
left2 = BinaryTreeNode("4")
right2 = BinaryTreeNode("5")

left3 = BinaryTreeNode("6")
right3 = BinaryTreeNode("7")

root = BinaryTreeNode("1")
#conectando los  nodos al arbol

root.left = childrenLeft
root.right= childrenRight

root.left.left = left2
root.right.left = left3

root.left.right = right2
root.right.right = right3


#tree.
#tree.left.right = right2

#tree.
#tree


result = []

preOrderRecursive(root, result)
print(result)
