# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
from heapq import heappush, heappop

class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.maxHeap = []
        self.minHeap = []

    def insert(self, number):
        if not self.maxHeap and not self.minHeap:
            heappush(self.minHeap, number)
            self.median = number
            return
        if number > self.minHeap[0]:
            heappush(self.minHeap, number)
            if len(self.minHeap) > len(self.maxHeap) + 1:
                p = heappop(self.minHeap)
                heappush(self.maxHeap, p * -1)
        else:
            heappush(self.maxHeap, -1 * number)
            if len(self.maxHeap) > len(self.minHeap) + 1:
                p = heappop(self.maxHeap)
                heappush(self.minHeap, -1 * p)
        if len(self.minHeap) > len(self.maxHeap):
            self.median = self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            self.median = self.maxHeap[0] * -1
        else:
            self.median = (self.minHeap[0] + self.maxHeap[0] * -1) / 2

    def getMedian(self):
        return self.median
