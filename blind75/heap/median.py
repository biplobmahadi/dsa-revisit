from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -1 * num)
        if self.large and self.large[0] < -1 * self.small[0]:
            heappush(self.large, -1 * heappop(self.small))
        if len(self.large) > len(self.small):
            heappush(self.small, -1 * heappop(self.large))
        if len(self.small) > len(self.large):
            heappush(self.large, -1 * heappop(self.small))

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -1 * self.small[0]
        else: 
            return (self.large[0] + (-1 * self.small[0])) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()