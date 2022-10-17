class BinaryTreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child

#RECORRIDOS


def preOrderRecursive(root, result):

    if not root:
        return

    result.append(root.data)    # D : data

    preOrderRecursive(root.left, result)  # L : left

    preOrderRecursive(root.right, result)  # R : right



'''
Binary Tree
 
                      1
                      |
            ----------------------
            |                     | 
            2                     3  
     ----------             ------------
     |        |             |          |
     4        5             6          7

    preorder: D.L.R [1, 2, 4, 5, 3, 6, 7]
  
'''


tree = BinaryTreeNode(1)

childrenLeft = BinaryTreeNode(2)
childrenRight = BinaryTreeNode(3)

childrenLeft2 = BinaryTreeNode(4)
childrenRight2 = BinaryTreeNode(7)

childrenLeft3 = BinaryTreeNode(5)
childrenRight3 = BinaryTreeNode(6)


tree.left = childrenLeft
tree.right = childrenRight
#--->
tree.left.left = childrenLeft2
tree.right.right = childrenRight2

tree.left.right = childrenLeft3
tree.right.left = childrenRight3



resultado_preorder = []

preOrderRecursive(tree, resultado_preorder)

print("PreOrder --> ", resultado_preorder)
