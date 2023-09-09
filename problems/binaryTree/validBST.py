def dfs(root, list):
    if root.left:
        dfs(root.left, list)
    list.append(root.val)
    if root.right:
        dfs(root.right, list)

def isValidBST(root):
    if not root:
        return True
    list = []
    dfs(root, list)
    i, j = 0, 1
    while j < len(list):
        if list[i] >= list[j]:
            return False
        i+=1
        j+=1
    return True

import math

def isValidBSTOptimal(root):
    if not root:
        return True
    return dfsPre(root, -math.inf, math.inf)

def dfsPre(root, greater, lesser):
    if not (root.val > greater and root.val < lesser):
        return False
    if root.left:
        if not (dfsPre(root.left, greater, root.val)):
            return False
    if root.right:
        if not (dfsPre(root.right, root.val, lesser)):
            return False
    return True