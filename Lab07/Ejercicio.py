
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

tree = BinaryTreeNode("Estudiante")

left = BinaryTreeNode("Aprobado")
right = BinaryTreeNode("Desaprobado")

# los nodos nuevos
left2 = BinaryTreeNode("Excelente")
right2 = BinaryTreeNode("Bueeno")


left3 = BinaryTreeNode("Regular")
right3 = BinaryTreeNode("Deficiente")
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



# Imprimir los valores del arbol
#para esto necesita incovar primero a la data principal es este caso al padre que es "Estudiante", luego los hijos indiz¿candoles a que rama pertenercen es decir si a la izquierda o derecha "REVISALO BIEN"


#1er intentoht().getD
