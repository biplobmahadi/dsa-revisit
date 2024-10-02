import math


def validBST(root):
    return check(root, -math.inf, math.inf)

def check(root, small, large):
    if not root: return True
    if root.val <= small or root.val >= large: return False
    return check(root.left, small, root.val) and check(root.right, root.val, large)
