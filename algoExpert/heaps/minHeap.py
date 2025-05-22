# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        c = (len(array)-2) // 2
        for i in reversed(range(c+1)):
            self.siftDown(i, len(array)-1, array)
        return array

    def siftDown(self, i, e, array):
        l = i*2 + 1
        while l <= e:
            r = i*2 + 2
            if r <=e and array[l] > array[r] < array[i]:
                array[r], array[i] = array[i], array[r]
                i = r
            elif array[l] < array[i]:
                array[l], array[i] = array[i], array[l]
                i = l
            else:
                break
            l = i*2 + 1

    def siftUp(self):
        l = len(self.heap)-1 
        while l > 0:
            p = (l-1) // 2
            if self.heap[p] > self.heap[l]:
                self.heap[p], self.heap[l] = self.heap[l], self.heap[p]
                l = p
            else:
                break

    def peek(self):
        return self.heap[0]

    def remove(self):
        val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return val

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()
