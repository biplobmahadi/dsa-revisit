import math

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    if not tree.left and not tree.right:
        return tree.value
    l = evaluateExpressionTree(tree.left)
    r = evaluateExpressionTree(tree.right)
    if tree.value == -1:
        return l+r
    elif tree.value == -2:
        return l - r
    elif tree.value == -3:
        return math.trunc(l/r)
    else:
        return l*r
