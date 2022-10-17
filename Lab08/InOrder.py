#In order--> LDR

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):

        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child


def InOrderRecursive(root, result):

    if not root:
        return

    InOrderRecursive(root.left, result)
    result.append(root.data)
    InOrderRecursive(root.right, result)

        
    '''
Binary Tree : Inorder Traversal
 
                      1
                      |
            ----------------------
            |                     | 
            2                     3  
            |                     | 
       ----------            ------------          
       |        |            |          |
       4        5            6          7
 
     --> 4 2 5 1 6 3 7 
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
root.right = childrenRight

root.left.left = left2
root.right.left = left3

root.left.right = right2
root.right.right = right3


#tree.
#tree.left.right = right2

#tree.
#tree


result = []

InOrderRecursive(root, result)
print(result)


