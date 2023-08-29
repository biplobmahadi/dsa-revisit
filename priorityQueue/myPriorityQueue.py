class MyMaxHeap():
    def __init__(self) -> None:
        self.data = []
    
    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        l = len(self.data)
        if l > 0:
            return False
        return True
        
    def _getParent(self, i):
        return (i - 1) // 2
    
    def _getLeft(self, i):
        return (i*2) + 1
    
    def _getRight(self, i):
        return (i*2) + 2
    
    def _swap(self, i, j):
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp

    def insert(self, val):
        self.data.append(val)
        position = len(self.data) - 1
        while position > 0:
            parent = self._getParent(position)
            if self.data[parent] < self.data[position]:
                self._swap(parent, position)
                position = parent
            else:
                break
        return self.data
    
    def delete(self):
        tmp = self.data[0]
        self.data[0] = self.data[len(self.data) - 1]
        self.data.pop()
        l = len(self.data) - 1
        position = 0
        while position < l:
            left = self._getLeft(position)
            right = self._getRight(position)
            
            if left <= l or right <= l:
                if right <= l:
                    if self.data[left] > self.data[right]:
                        if self.data[left] > self.data[position]:
                            self._swap(left, position)
                            position = left
                        else:
                            break
                    else:
                        if self.data[right] > self.data[position]:
                            self._swap(right, position)
                            position = right
                        else:
                            break
                else:
                    if self.data[left] > self.data[position]:
                        self._swap(left, position)
                        position = left
                    else:
                        break
            else:
                break
        return tmp
    
class MyPriorityQueue:
    def __init__(self) -> None:
        self.heap = MyMaxHeap()

    def enqueue(self, val):
        return self.heap.insert(val)
    
    def dequeue(self):
        return self.heap.delete()
    
    def size(self):
        return self.heap.size()
    
myPriorityQueue = MyPriorityQueue()

myPriorityQueue.enqueue(45)
myPriorityQueue.enqueue(35)
myPriorityQueue.enqueue(30)
myPriorityQueue.enqueue(32)
myPriorityQueue.enqueue(25)
myPriorityQueue.enqueue(28)
myPriorityQueue.enqueue(88)
print(myPriorityQueue.dequeue())
print(myPriorityQueue.dequeue())
print(myPriorityQueue.dequeue())

print(myPriorityQueue.heap.data)