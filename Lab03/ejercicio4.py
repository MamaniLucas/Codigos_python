class LinkedLsit:


    def __init__(self):
        self.head = None
        self.length = 0

    def print( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next
        print("NULL")


    def insertAtPos(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBegin(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = None()
                    newNode.data = data
                    count = 0
                    current = self.head
                    while count < pos-1:
                        count += 1
                        current = current.next

                    newNode.next = current.next
                    current.next = newNode
                    self.length += 1

