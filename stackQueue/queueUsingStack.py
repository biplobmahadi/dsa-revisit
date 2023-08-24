class MyStack: 
    def __init__(self) -> None:
        self.data = []
    
    def push(self, val):
        self.data.append(val)
        return self.data

    def pop(self):
        popped = self.data.pop()
        return  popped
    
    def peak(self):
        return self.data[len(self.data) - 1]
    

class Queue: 
    def __init__(self) -> None:
        self.stack1 = MyStack()
        self.stack2 = MyStack()
    
    def enqueue(self, val):
        self.stack1.push(val)
        return self.stack1
    
    def dequeue(self):
        for i in range(0, len(self.stack1.data)):
            self.stack2.push(self.stack1.pop())
        popped = self.stack2.pop()
        for i in range(0, len(self.stack2.data)):
            self.stack1.push(self.stack2.pop())
        return popped
    
    def peak(self):
        for i in range(0, len(self.stack1.data)):
            self.stack2.push(self.stack1.pop())
        peaked = self.stack2.peak()
        for i in range(0, len(self.stack2.data)):
            self.stack1.push(self.stack2.pop())
        return peaked
    
queue = Queue()

queue.enqueue(4)
queue.enqueue(42)
queue.enqueue(43)

print(queue.dequeue())
queue.enqueue(32)
print(queue.peak())
print(queue.dequeue())
print(queue.peak())
print(queue.stack1.data)
