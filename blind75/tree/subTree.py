def sameTree(p, q):
    if not p and not q: return True
    if not p or not q or p.val != q.val: return False
    return sameTree(p.left, q.left) and sameTree(p.right, q.right)

def subTree(root, subRoot):
    if not root: return False
    if sameTree(root, subRoot): return True
    return subTree(root.left, subRoot) or subTree(root.right, subRoot)
