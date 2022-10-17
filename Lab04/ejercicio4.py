class Node:

    # Constructor
    def __init__(self):
        self.data = None
        self.next = None

    # return true if thenode point to another node
    def hasNext(self):
        return self.next != None


# Stack Linked List
class StackLinkedList:

    # Constructor
    def __init__(self, data=None):
        self.head = None
        if data:
            for d in data:
                self.push(d)

    def push(self, data):
        temp = Node()
        temp.data = data
        temp.next = self.head
        self.head = temp

    def pop(self):
        if self.head is None:  # la lista enlazada es vacia?
            #raise IndexError   # throw new Exception()
            print(" Underflow")
            return -1
        temp = self.head.data
        self.head = self.head.next
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.data

    def print(self):
        node = self.head
        while node != None:
            print(node.data, end=" => ")
            node = node.next
        print("NULL")

    # Get length of linked list
    def listLength(self):

        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.next

        return count

  
our_stack = StackLinkedList()
our_stack.push(1)
our_stack.push(21)

our_stack.print()
print("length : ", our_stack.listLength())
print(our_stack.pop())
print(our_stack.pop())
