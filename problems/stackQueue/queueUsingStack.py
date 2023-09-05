class MyQueue:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)
    
    def pop(self):
        for i in range(0, len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        popped = self.stack2.pop()
        for i in range(0, len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return popped
    
    def peek(self):
        for i in range(0, len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        peeked = self.stack2[len(self.stack2) - 1]
        for i in range(0, len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return peeked
    
    def empty(self):
        return len(self.stack1) == 0


class MyQueueAmortized:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)
    
    def pop(self):
        self.peek()
        return self.stack2.pop()
    
    def peek(self):
        if not self.stack2:
            for i in range(0, len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def empty(self):
        return not (self.stack1 or self.stack2)
    

