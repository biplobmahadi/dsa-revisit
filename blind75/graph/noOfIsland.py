def noIslands(grid):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def dfs(r, c):
        if (r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or
            grid[r][c] == '0'): 
            return 0
        grid[r][c] = '0'
        for nr, nc in directions:
            dfs(r+nr, c+nc)
        return 1
    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            res += dfs(r, c)
    return res

print(noIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))