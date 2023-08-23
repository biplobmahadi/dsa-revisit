class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class MyDoublyLL: 
    def __init__(self, val):
        node = Node(val)
        self.head = node
        self.tail = self.head
        self.length = 1

    def print(self):
        list = [] 
        currentNode = self.head

        while currentNode is not None:
            list.append(currentNode.value)
            currentNode = currentNode.next
        return list
    
    def append(self, val):
        node = Node(val)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length +=1
        return self.length

    def prepend(self, val):
        node = Node(val)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1
        return self.length

    def getLeader(self, idx):
        leader = self.head
        for i in range(0, idx -1):
            leader = leader.next
        return leader
    
    def insert(self, idx, val):
        if idx <= 0:
            self.prepend(val)
        elif idx >= self.length:
            self.append(val)
        else:
            node = Node(val)
            leader = self.getLeader(idx)
            follower = leader.next
            leader.next = node
            node.next = follower
            node.prev = leader
            follower.prev = node
            self.length += 1
        return self.length

    def remove(self, idx):
        if(idx >= 0 and idx < self.length):
            leader = self.getLeader(idx)
            current = leader.next
            follower = current.next
            leader.next = follower
            follower.prev = leader
            self.length -= 1
        return self.length
    
    def __str__(self):
        return f'len is: {self.length}'


myDoublyLL = MyDoublyLL(3)
myDoublyLL.append(4)
myDoublyLL.append(5)
myDoublyLL.prepend(2)
myDoublyLL.insert(-1, 8)
myDoublyLL.insert(2, 84)
myDoublyLL.insert(6, 843)
myDoublyLL.remove(2)

print(myDoublyLL)
print(myDoublyLL.print())