# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    res, val = [0], [0]
    def solve(tree, k):
        if not tree: return 0
        if tree.right: 
            curr = solve(tree.right, k)
            if curr == 'T':
                return 'T'
        val[0] += 1
        if val[0] == k:
            res[0] = tree.value
            return 'T'
        if tree.left: 
            curr = solve(tree.left, k)
            if curr == 'T':
                return 'T'
        return val
    solve(tree, k)
    return res[0]
