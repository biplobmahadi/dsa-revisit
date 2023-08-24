class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class StackLL:
    def __init__(self, val):
        node = Node(val)
        self.head = node
        self.tail = self.head
        self.length = 1
    
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.length += 1
        return self.length
    
    def pop(self):
        popped = self.head
        self.head = self.head.next
        self.length -=1
        return popped

    def print(self):
        list = [] 
        currentNode = self.head

        while currentNode is not None:
            list.append(currentNode.value)
            currentNode = currentNode.next
        return list
    
    def peak(self):
        return self.head
    
    def __str__(self):
        return f'len is: {self.length}'

    
stackLL = StackLL(3)
stackLL.push(40)
stackLL.push(43)
stackLL.push(44)
print(stackLL.pop().value)
print(stackLL.pop().value)
print(stackLL.peak().value)

print(stackLL)
print(stackLL.print())
