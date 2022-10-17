class QueueDynamicArray:

    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size <= 0

    def enQueue(self, item):
        if self.size >= self.limit:
            self.resize()
        self.que.append(item)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1
        print('Queue after enQueue', self.que)

    def deQueue(self):
        if self.size <= 0:
            print('Qeue Underflow....!')
            raise IndexError  # Lanza una excepcion controlada , OPCIONAL : return -1
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            print('Queue after deQueue', self.que)

    def queueRear(self):
        if self.rear is None:
            print('Sorry, the queue is empty..!')
            raise IndexError  # Lanza una excepcion controlada , OPCIONAL : return -1
        return self.que[self.rear]

    def queueFront(self):
        if self.front is None:
            print('Sorry, the queue is empty')
            raise IndexError  # Lanza una excepcion controlada , OPCIONAL : return -1
        return self.que[self.front]

    def getSize(self):
        return self.size

    def resize(self):
        # newQue = list(self.que)
        self.limit = 2 * self.limit
        # self.que = newQue

    def getQue(self):
        return self.que

    def getLimit(self):
        return self.limit


# Execution

 
# Execution
que = QueueDynamicArray(10)
 
data = ["first","second","third","fourth",
        "fifth","sixth","seventh","eighth"]
 
for item in data:


    print("--------------------------------")
    que.enQueue(item)
    print("Que    --> ", que.getQue())
    print("Front  --> ", que.queueFront())
    print("Rear   --> ", que.queueRear())
    print("Limit  --> ", que.getLimit())
    print("Size   --> ", que.getSize())

    print("--------------------------------")
    que.enQueue(item)
    print("Que    --> ", que.getQue())
    print("Front  --> ", que.queueFront())
    print("Rear   --> ", que.queueRear())
    print("Limit  --> ", que.getLimit())
    print("Size   --> ", que.getSize())

    print("--------------------------------")
    que.enQueue(item)
    print("Que    --> " , que.getQue())
    print("Front  --> " , que.queueFront())
    print("Rear   --> " , que.queueRear())
    print("Limit  --> " , que.getLimit())
    print("Size   --> " , que.getSize())

    print("--------------------------------")
    que.enQueue(item)
    print("Que    --> " , que.getQue())
    print("Front  --> " , que.queueFront())
    print("Rear   --> " , que.queueRear())
    print("Limit  --> " , que.getLimit())
    print("Size   --> " , que.getSize())
    print("--------------------------------")

    print("--------------------------------")
    que.deQueue()
    print("Que    --> " , que.getQue())
    print("Front  --> " , que.queueFront())
    print("Rear   --> " , que.queueRear())
    print("Limit  --> " , que.getLimit())
    print("Size   --> " , que.getSize())
    

