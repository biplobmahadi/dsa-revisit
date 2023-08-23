class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class MySinglyLL: 
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
        self.tail = node
        self.length +=1
        return self.length

    def prepend(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.length += 1
        return self.length

    def insert(self, idx, val):
        if idx <= 0:
            self.prepend(val)
        elif idx >= self.length:
            self.append(val)
        else:
            i, parent = 1, self.head
            while i is not idx:
                i += 1
                parent = parent.next
            node = Node(val)
            node.next = parent.next
            parent.next = node
            self.length+= 1
        return self.length

    def remove(self, idx):
        if(idx >= 0 and idx < self.length):
            i, parent = 1, self.head
            while i is not idx:
                i += 1 
                parent = parent.next
            parent.next = parent.next.next
            self.length -= 1
        return self.length
    
    def reverse(self):
        current = self.head
        hold = None
        self.tail = current
        while current is not None:
            nextNode = current.next
            current.next = hold
            hold = current
            current = nextNode
        self.head = hold
        return None

    def __str__(self):
        return f'len is: {self.length}'


mysinglyLL = MySinglyLL(3)
mysinglyLL.append(4)
mysinglyLL.append(5)
mysinglyLL.prepend(2)
mysinglyLL.insert(-1, 8)
mysinglyLL.insert(2, 84)
mysinglyLL.insert(6, 843)
mysinglyLL.remove(2)

mysinglyLL.reverse()
print(mysinglyLL)
print(mysinglyLL.print())
