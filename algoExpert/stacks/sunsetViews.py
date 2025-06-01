from collections import deque

def sunsetViews(buildings, direction):
    if not buildings: return []
    q = deque()
    if direction == 'EAST':
        goLeft(buildings, q)
    else:
        goRight(buildings, q)
    return list(q)

def goLeft(b, q):
    last = b[len(b)-1]
    q.appendleft(len(b)-1)
    for i in reversed(range(len(b)-1)):
        curr = b[i]
        if curr > last:
            last = curr
            q.appendleft(i)

def goRight(b, q):
    last = b[0]
    q.append(0)
    for i in range(1, len(b)):
        curr = b[i]
        if curr > last:
            last = curr
            q.append(i)
