grid = [
    [3, 2, 5, 23],
    [34, 2, 1, 43],
    [75, 755, 453, 2],
    [334, 52, 121, 231],
]

directions = [[-1, 0],[0, 1], [1, 0], [0, -1]]
def dfs(grid, row, col, visited):
    if (row < 0 or col < 0 or row >= len(grid) or 
        col >= len(grid[0]) or (row, col) in visited
        ): return
    
    print(grid[row][col])
    visited.add((row, col))
    for r, c in directions:
        dfs(grid, row+r, col+c, visited)

dfs(grid, 0, 0, set())

