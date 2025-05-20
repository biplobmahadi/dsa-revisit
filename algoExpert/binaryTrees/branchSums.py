# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if not root: return []
    res = []
    def solve(root, s):
        s += root.value
        if not root.left and not root.right:
            res.append(s)
            return
        if (root.left): solve(root.left, s)
        if (root.right): solve(root.right, s)
        s-= root.value
    solve(root, 0)
    return res
