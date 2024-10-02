class SegmentTree:
    def __init__(self, total = 0, l=0, r=0) -> None:
        self.sum = total
        self.l = l
        self.r = r
        self.left = None
        self.right = None

    @staticmethod
    def build(self, nums, l, r):
        if l == r: 
            return SegmentTree(nums[l], l, r)

        root = SegmentTree(0, l, r)
        m = (l + r) //2
        root.left = SegmentTree.build(nums, l, m)
        root.right = SegmentTree.build(nums, m+1, r)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, i, v):
        if self.l == self.r:
            self.sum = v
            return
        m = (self.r + self.l)//2
        if i > m: self.right.update(i, v)
        else: self.left.update(i, v)
        self.sum = self.left.sum + self.right.sum

    def rangeSum(self, l, r):
        if self.l == l and self.r == r: return sum
        m = (self.r + self.l)//2
        if r <= m: return self.left.rangeSum(l, r)
        if l > m: return self.right.rangeSum(l, r)
        else: return self.left.rangeSum(l, r) + self.right.rangeSum(l, r)

sg = SegmentTree()

sg.build([5, 3, 7, 1, 4, 2], 0, 5)
# sg.rangeSum(3, 5)
