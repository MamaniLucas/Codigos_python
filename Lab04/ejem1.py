#class node:para node
class Node:
   def __init__(self):
    self.data=None
    self.next = None

   def hasNext(self):
       return self.next != None


class StackLinkedList:
   
    def __init__(self, data = None):
        self.head = None
        if data:
            for d in data:
                self.push(d)

#deefinir el objto de la clse node
   
    def push(self, data):
        temp = Node()
        temp.data=data
        temp.next =self.head
        self.head = temp

        #salida 
    def pop(self):

        if self.head is None:
            print("underflow")
            return -1 
        temp = self.head.data
        self.heas=self.head.next
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.data

    def print(self):
        node=self.head
        while node != None:
            print(node.data, end=" => ")
            node = node.next
        print("NULL")

    def listLength(self):
        current = self.head
        count=0

        while current != None:
            count = count +1
            current=current.next
        return count

#bucle o lop ciclo whilesimple, dinamico, listasenlazadas.

our_stack = StackLinkedList()
our_stack.push(1)
our_stack.push(21)
our_stack.push(14)
our_stack.push(31)
our_stack.push(19)
our_stack.push(3)
our_stack.push(99)
our_stack.push(9)

our_stack.print()
print("length: ", our_stack.listLength())
print(our_stack.pop())
print(our_stack.pop())
print("length: ", our_stack.listLength())

