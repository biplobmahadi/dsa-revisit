class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class QueueLL:
    def __init__(self, val):
        node = Node(val)
        self.head = node
        self.tail = self.head
        self.length = 1
    
    def enqueue(self, val):
        node = Node(val)
        self.tail.next = node
        self.tail = node
        self.length +=1
        return self.length
    
    def dequeue(self):
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

    
queueLL = QueueLL(3)
queueLL.enqueue(40)
queueLL.enqueue(43)
queueLL.enqueue(44)
print(queueLL.dequeue().value)
print(queueLL.dequeue().value)
print(queueLL.peak().value)

print(queueLL)
print(queueLL.print())
