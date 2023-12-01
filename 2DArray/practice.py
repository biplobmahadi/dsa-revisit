# count the unique paths from the top left to 
# bottom right, only 0's can be path

def dfs(grid, r, c):
    if (r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or
        grid[r][c] == 1):
        return 0
    if r == len(grid)-1 and c == len(grid[0])-1:
        return 1
    grid[r][c] = 1
    count = 0
    count+= dfs(grid, r+1, c)
    count+= dfs(grid, r-1, c)
    count+= dfs(grid, r, c+1)
    count+= dfs(grid, r, c-1)
    grid[r][c] = 0
    return count

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
]

print(dfs(grid, 0, 0)) # O(4^m*n), O(m*n)


# find the min path lenght of same given question
# bfs total level is the min len
from collections import deque
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(grid):
    l = 0
    q = deque()
    q.append((0,0))
    grid[0][0] = 1

    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if r == len(grid)-1 and c == len(grid[0])-1:
                return l
            for dr, dc in directions:
                nwr = r+dr
                nwc = c+dc
                if (nwr>=0 and nwc>=0 and nwr<len(grid) and
                    nwc<len(grid[0]) and grid[nwr][nwc]!=1):
                    q.append((nwr, nwc))
                    grid[nwr][nwc] = 1
        l+=1

print(bfs(grid))
