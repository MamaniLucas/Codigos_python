

class BinaryTreeNode:

    def _init_(self, data, left=None, right=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child

#seteas los valores de la data la cual estas trabajando
    def setData(self, data):
        self.data = data
#con el get optienes aquellos valores  de la derecha y izquierda

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


# Forma 1
left = BinaryTreeNode("Aprobado")
right = BinaryTreeNode("Desaprobado")
tree = BinaryTreeNode("Estudiante", left, right)


# Forma 2
left = BinaryTreeNode("Aprobado")
right = BinaryTreeNode("Desaprobado")
tree1 = BinaryTreeNode("Estudiante")
tree1.left = left
tree1.right = right

# Imprimir los valores del arbol
#para esto necesita incovar primero a la data principal es este caso al padre que es "Estudiante", luego los hijos indiz¿candoles a que rama pertenercen es decir si a la izquierda o derecha "REVISALO BIEN"

#1er intento
print(tree.getData())
print(tree.getLeft().getData())
print(tree.getRight().getData())
print("----------SEGUNDA MANERA------------")
#2er intento
print(tree1.getData())
print(tree1.getLeft().getData())
print(tree1.getRight().getData())
