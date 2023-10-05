class PrefixSum:
    def __init__(self, nums) -> None:
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
        
    def rangeSum(self, l, r):
        if r >= len(self.prefix) or l < 0:
            raise IndexError('not valid range')
        preRight = self.prefix[r]
        preLeft = self.prefix[l-1] if l>0 else 0
        return preRight - preLeft

p = PrefixSum([2, -1, 3, -3, 4])
print(p.rangeSum(1, 4))