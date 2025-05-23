# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    def solve(one, two):
        if not one and not two:
            return None
        v1 = one.value if one else 0
        v2 = two.value if two else 0
        n = BinaryTree(v1+v2)
        n.left = solve(one.left if one else None, two.left if two else None)
        n.right = solve(one.right if one else None, two.right if two else None)
        return n
    return solve(tree1, tree2)


def mergeBinaryTrees2(tree1, tree2):
    if not tree1:
        return tree2
    if not tree2:
        return tree1
    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree1
