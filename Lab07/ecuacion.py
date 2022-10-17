

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
 
                      *
                      |
            ----------------------
            |                     | 
            -                     -  
            |                     | 
       ----------            ------------          
       |        |            |          |
      10         3           12         3
 
     --> ( 10  - 3 ) * ( 12 – 3 ) 
'''


childrenLeft = BinaryTreeNode("-")
childrenRight = BinaryTreeNode("-")
# los nodos nuevos
left2 = BinaryTreeNode("10")
right2 = BinaryTreeNode("3")

left3 = BinaryTreeNode("12")
right3 = BinaryTreeNode("3")

root = BinaryTreeNode("*")
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
