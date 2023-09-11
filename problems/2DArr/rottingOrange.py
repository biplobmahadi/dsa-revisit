from collections import deque

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]

def orangeRotting(grid: list[list[int]]) -> int:
    if not (grid and grid[0]): return 0
    count, queue = 0, deque()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                queue.append([row, col])
    while queue:
        lenght = len(queue)
        for _ in range(lenght):
            popped = queue.popleft()
            currRow, currCol = popped[0], popped[1]
            for dir in directions:
                nextRow, nextCol = dir[0] + currRow, dir[1] + currCol
                if (nextRow>=0 and nextCol>=0 and nextCol<len(grid[0]) and 
                    nextRow<len(grid) and grid[nextRow][nextCol] == 1):
                    queue.append([nextRow, nextCol])
                    grid[nextRow][nextCol] = 2
        count+=1
    countFresh = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                countFresh+=1
    if countFresh:
        return -1
    elif count:
        return count-1
    return 0

grid = [[0]]
print(orangeRotting(grid))
