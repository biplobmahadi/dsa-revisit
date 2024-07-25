from collections import deque

adjacencyList = [[2, 3], [5], [0, 5, 4], [0, 4], [2, 3, 5], [1, 2, 4]]


def bfs():
    queue = deque()
    queue.append(0)
    visited = set()
    visited.add(0)

    while queue:
        p = queue.popleft()
        print(p)
        for n in adjacencyList[p]:
            if n not in visited:
                queue.append(n)
                visited.add(n)

bfs()