def nodeDepths(root):
    res = [0]
    def solve(root, c):
        if not root:
            return
        res[0]+=c
        solve(root.left, c+1)
        solve(root.right, c+1)
    solve(root, 0)
    return res[0]


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
