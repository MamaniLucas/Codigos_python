class queueList:

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



lista=queueList






print("Listado de compras")
cola = ["Camote", "lechuga"]
print(cola)

        #agregar a la cola
print(" Agregando a Listado de compras")

cola.append("PAN")
print("Se necesita:", cola[-1])
cola.append("Mantequilla")
print("Se necesita:", cola[-1])
cola.append("Cebolla")
print("Se necesita:", cola[-1])
cola.append("Tomate")
print("Se necesita:", cola[-1])
cola.append("Brocolí")
print("Se necesita:", cola[-1])

print(cola)
        #eliminar

print("SALIDA")

atendido = cola.pop(0)
print("Se compro:", atendido)
atendido = cola.pop(0)
print("Se compro:", atendido)
atendido = cola.pop(0)
print("Se compro:", atendido)
atendido = cola.pop(0)
print("Se compro:", atendido)


        #esta vacia al no tener elemetnos
        # ver el tamaño
print(cola)

cola.append("PAN")
print("Se necesita:", cola[-1])
cola.append("Mantequilla")
print("Se necesita:", cola[-1])
print(cola)
