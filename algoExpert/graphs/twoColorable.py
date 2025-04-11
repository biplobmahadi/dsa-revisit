from collections import deque

def twoColorable(edges):
    if len(edges) == 1: return False
    q = deque()
    q.append(0)
    visit = set()
    visit.add(0)
    adj = {}
    adj[0] = 1
    while q:
        p = q.popleft()
        for n in edges[p]:
            if n in adj and adj[n] == adj[p]:
                return False
            if n not in visit:
                q.append(n)
                adj[n] = 1 if adj[p] == 2 else 2
                visit.add(n)
    return True
