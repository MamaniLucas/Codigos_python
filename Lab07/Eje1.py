


class BinaryTreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child


# Forma 1

# Forma 2
tree1 = BinaryTreeNode("Estudiante")
left = BinaryTreeNode("Aprobado")
right = BinaryTreeNode("Desaprobado")
tree1.left = left
tree1.right = right

# Imprimir los valores del arbol
#para esto necesita incovar primero a la data principal es este caso al padre que es "Estudiante", luego los hijos indiz¿candoles a que rama pertenercen es decir si a la izquierda o derecha "REVISALO BIEN"


print(tree1.data)

print(tree1.left.data)

print(tree1.right.data)

#1er intentoht().getData())