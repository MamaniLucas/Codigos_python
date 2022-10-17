#🡺 L.D.R
class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child

# In-order recursive traversal. The
# nodes' values are appended to the
# result list in traversal order
def inOrderRecursive(root, result):

    if not root:
        return

    inOrderRecursive(root.left, result)
    result.append(root.data)
    inOrderRecursive(root.right, result)

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
root = BinaryTreeNode("Estudiante",childrenLeft,childrenRight)
 
result = []
inOrderRecursive(root, result)
print(result)
