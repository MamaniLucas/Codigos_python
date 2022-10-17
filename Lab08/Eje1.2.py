#-> L_R_D

class BinaryTreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child

# Post-order recursive traversal. The
# nodes' values are appended to the
# result list in traversal order


def postOrderRecursive(root, result):

    if not root:
        return

    postOrderRecursive(root.left, result)
    postOrderRecursive(root.right, result)
    result.append(root.data)


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
postOrderRecursive(root, result)
print(result)
