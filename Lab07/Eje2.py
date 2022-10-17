

class BinaryTreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child


def postOrderRecursive(root, result):
    if not root:
        return
    postOrderRecursive(root.left, result)
    postOrderRecursive(root.right, result)
    result.append(root.data)


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

# Forma 2

#Creamos los nodos tipo BynariTree
tree1 = BinaryTreeNode("Estudiante")
left = BinaryTreeNode("Aprobado")
right = BinaryTreeNode("Desaprobado")

#Enlazamos los nodos para crear el árbol
tree1.left = left
tree1.right = right

resultado_preorder = []
resultado_postorder = []
resultado_inorder = []

preOrderRecursive(tree1, resultado_preorder)
postOrderRecursive(tree1, resultado_postorder)
inOrderRecursive(tree1, resultado_inorder)

print("PreOrder --> ", resultado_preorder)
print("PostOrder --> ", resultado_postorder)
print("InOrder --> ", resultado_inorder)

