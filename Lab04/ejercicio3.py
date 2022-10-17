class StackDynamicArray:

    # Constructor
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print('Stack after Push', self.stk)

    def pop(self):
        if len(self.stk) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print('Stack Underflow!')
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

    def resize(self):
        self.limit = 2 * self.limit
        #self.stk = list(self.stk)


if __name__ == "__main__":

    our_stack = StackDynamicArray(15)
    our_stack.push(1)
    our_stack.push(2)
    our_stack.push(3)
    our_stack.push(4)
    our_stack.push(5)
    our_stack.push(6)
    our_stack.push(7)
    our_stack.push(8)
    our_stack.push(9)
    our_stack.push(10)
    our_stack.push(11)
    our_stack.push(12)
    our_stack.push(13)
    our_stack.push(14)
    our_stack.push(1)
    our_stack.push(2)
    our_stack.push(3)
    our_stack.push(4)
    our_stack.push(5)
    our_stack.push(6)
    our_stack.push(7)
    our_stack.push(8)
    our_stack.push(9)
    our_stack.push(10)
    our_stack.push(11)
    our_stack.push(12)
    our_stack.push(13)
    our_stack.push(14)
print(our_stack.peek())
print(our_stack.pop())
print(our_stack.peek())
print(our_stack.pop())
