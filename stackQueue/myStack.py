# my stack using list

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
    
myStack = MyStack()

print(myStack.push(2))
print(myStack.push(22))
print(myStack.push(222))
print(myStack.push(2222))
print(myStack.pop())
print(myStack.pop())
print(myStack.peak())
print(myStack.data)