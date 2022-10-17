class BinaryTreeNode:

    def __init__(self, data, left=None, right=None, medio=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child

#RECORRIDOS


def preOrderRecursive(root, result):

    if not root:
        return

    result.append(root.data)
    preOrderRecursive(root.left, result)
    preOrderRecursive(root.right, result)


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
            ---------------------------------------
            |                                    | 
         Aprobado                         Desaprobado  
      ----------------                ------------------------
    |                 |               |                      |
Excelente           Bueno         Regular              Deficiente
'''

# Forma 2

#Creamos los nodos tipo BynariTree
tree = BinaryTreeNode("Numero")

left = BinaryTreeNode("Par")
right = BinaryTreeNode("Impar")

left2 = BinaryTreeNode("<=100")
right2 = BinaryTreeNode(">100")

left3 = BinaryTreeNode("<=50")
right3 = BinaryTreeNode(">50")


#Enlazamos los nodos para crear el árbol
tree.left = left
tree.right = right

tree.left.left = left2
tree.left.right = right2

tree.right.left = left3
tree.right.right = right3

resultado_preorder = []
resultado_postorder = []
resultado_inorder = []

preOrderRecursive(tree, resultado_preorder)
postOrderRecursive(tree, resultado_postorder)
inOrderRecursive(tree, resultado_inorder)

print("PreOrder --> ", resultado_preorder)
print("PostOrder --> ", resultado_postorder)
print("InOrder --> ", resultado_inorder)

