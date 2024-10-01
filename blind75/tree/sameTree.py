def sameTree(p, q):
    if not p and not q: return True
    if not p or not q or p.val != q.val: return False
    return sameTree(p.left, q.left) and sameTree(p.right, q.right)