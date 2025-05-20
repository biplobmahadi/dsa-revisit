# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    def solve(tree, l, r):
        if not tree:
            return True
        return l <= tree.value < r and solve(tree.left, l, tree.value) and solve(tree.right, tree.value, r)
    return solve(tree, float('-inf'), float('inf'))
    
