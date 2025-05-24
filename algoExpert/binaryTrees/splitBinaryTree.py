# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree(tree):
    s = sumF(tree)
    res = [0]
    def solve(tree):
        l = 0
        if tree.left:
            l = solve(tree.left)
            if not l: return
            if l == s - l:
                res[0] = l
                return 
        r = 0
        if tree.right:
            r = solve(tree.right)
            if not r: return
            if r == s - r:
                res[0] = r
                return 
        return tree.value + l + r
    solve(tree)
    return res[0]
    
def sumF(tree):
    if not tree:
        return 0
    l = sumF(tree.left)
    r = sumF(tree.right)
    return tree.value + l + r
    
