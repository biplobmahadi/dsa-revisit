# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    res = [0]
    def solve(tree):
        if not tree: return 0
        l = solve(tree.left)
        r = solve(tree.right)
        curr = l + r
        if curr > res[0]:
            res[0] = curr
        return l+1 if l>r else r+1
    solve(tree)
    return res[0]