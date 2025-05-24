# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    def solve(one, two):
        if not one and not two:
            return True
        if not one or not two or one.value != two.value:
            return False
        res1 = solve(one.left, two.right)
        if not res1:
            return False
        res2 = solve(one.right, two.left)
        if not res2:
            return False
        return True
    res = solve(tree.left, tree.right)

    return res
