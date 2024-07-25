from collections import deque

grid = [
    [3, 2, 5, 23],
    [34, 2, 1, 43],
    [75, 755, 453, 2],
    [334, 52, 121, 231],
]

directions = [[-1, 0],[0, 1], [1, 0], [0, -1]]

def bfs():
    r, c = 0, 0
    visited = set()
    queue = deque()
    queue.append((r, c))
    visited.add((r, c))

    while queue:
        pr, pc = queue.popleft()
        print(grid[pr][pc])
        for cr, cc in directions:
            row, col = pr + cr, pc + cc
            if (row >= 0 and col >= 0 and row < len(grid) and 
                col < len(grid[0]) and (row, col) not in visited
                ):
                queue.append((row, col))
                visited.add((row, col))

bfs()
