from collections import deque

directions = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]

def numOfIslands(grid):
    if not (grid and grid[0]): return 0
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                count+=1
                grid[row][col] = 0
                queue = deque([{'row': row, 'col': col}])
                while queue:
                    popped = queue.popleft()
                    currRow = popped.get('row')
                    currCol = popped.get('col')
                    for i in directions:
                        nextRow = currRow + i[0]
                        nextCol = currCol + i[1]
                        if (nextRow >= 0 and nextCol>=0 and nextRow<len(grid) and 
                            nextCol<len(grid[0]) and grid[nextRow][nextCol] == '1'):
                            queue.append({'row': nextRow, 'col': nextCol})
                            grid[nextRow][nextCol] = 0
    return count

grid = [["0","1","0"],
        ["1","0","1"],
        ["0","1","0"]]

print(numOfIslands(grid))
