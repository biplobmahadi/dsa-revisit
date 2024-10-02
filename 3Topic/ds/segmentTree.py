class Node:
    def __init__(self, total = 0, l=0, r=0) -> None:
        self.sum = total
        self.l = l
        self.r = r
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self) -> None:
        self.root = None

    def build(self, nums, l, r):
        if l == r: 
            return Node(nums[l], l, r)

        root = Node(0, l, r)
        m = (l + r) //2
        root.left = self.build(nums, l, m)
        root.right = self.build(nums, m+1, r)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, i, v, root):
        if root.l == root.r:
            root.sum = v
            return
        m = (root.r + root.l)//2
        if i > m: self.update(i, v, root.right)
        else: self.update(i, v,root.left)
        root.sum = root.left.sum + root.right.sum

    def rangeSum(self, l, r, root):
        if root.l == l and root.r == r: return root.sum
        m = (root.r + root.l)//2
        if r <= m: return self.rangeSum(l, r, root.left)
        if l > m: return self.rangeSum(l, r, root.right)
        else: return self.rangeSum(l, m, root.left) + self.rangeSum(m+1, r, root.right)

sg = SegmentTree()
sg.root = sg.build([5, 3, 7, 1, 4, 2], 0, 5)
print(sg.root.l, sg.root.r)
print(sg.rangeSum(1, 2, sg.root))
