def lowestCommonAncestor(root, p, q):
    curr = root
    while curr:
        if curr.val > p.val and curr.val > q.val:
            curr = curr.left
        elif curr.val < p.val and curr.val < q.val:
            curr = curr.right
        else: 
            return curr