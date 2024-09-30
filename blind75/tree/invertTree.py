def invert(root):
    if not root: return None
    tmp = root.left
    root.left = invert(root.right)
    root.right = invert(tmp)
    return root