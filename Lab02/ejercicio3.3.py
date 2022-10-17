# Node of a Single Linked List
class Node:

   # Constructor
   def __init__(self):
       self.data = None
       self.next = None

   # return true if the node point to another node

   def hasNext(self):
       return self.next != None
