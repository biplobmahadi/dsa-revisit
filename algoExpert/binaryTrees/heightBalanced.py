# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    def solve(tree):
        if not tree:
            return 0
        l = solve(tree.left) 
        if l == 'False':
            return 'False'
        r = solve(tree.right)
        if r == 'False':
            return 'False'
        if abs(l-r) > 1:
            return 'False'
        return max(l, r) + 1
    return True if solve(tree) != 'False' else False
