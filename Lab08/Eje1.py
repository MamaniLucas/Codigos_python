#🡺  D.L.R.
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
Binary Tree
 
                  Estudiante
                      |
            ----------------------
            |                     | 
         Aprobado            Desaprobado  
     
'''

childrenLeft = BinaryTreeNode("Aprobado")
childrenRight = BinaryTreeNode("Desaprobado")
root = BinaryTreeNode("Estudiante", childrenLeft, childrenRight)

result = []
preOrderRecursive(root, result)
print(result)
