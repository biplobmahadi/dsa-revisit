from collections import deque

def levelOrder(root):
    if not root: return []
    res = []
    q = deque()
    q.append(root)
    while q:
        level = []
        for _ in range(len(q)):
            p = q.popleft()
            level.append(p.val)
            if p.left: q.append(p.left)
            if p.right: q.append(p.right)
        res.append(level)
    return res

