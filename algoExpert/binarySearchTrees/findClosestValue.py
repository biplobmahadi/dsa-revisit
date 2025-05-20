def findClosestValueInBst(tree, target):
    l = float('inf')
    res = tree.value
    while tree:
        d = abs(tree.value - target)
        if l > d:
            res = tree.value
            l = d
        if tree.value<target:
            tree = tree.right
        else:
            tree = tree.left
    return res


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
