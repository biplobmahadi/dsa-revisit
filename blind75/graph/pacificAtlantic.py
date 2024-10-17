directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def dfs(ocean, r, c, prev, heights):
    if (r<0 or c<0 or r>=len(heights) or c>=len(heights[0]) or
        heights[r][c] < prev or (r, c) in ocean): return
    ocean.add((r, c))
    for nr, nc in directions:
        dfs(ocean, r+nr, c+nc, heights[r][c], heights)
    

class Solution:
    def pacificAtlantic(self, heights):
        atl, pac = set(), set()
        R, C = len(heights), len(heights[0])
        for r in range(R):
            dfs(atl, r, C-1, -1, heights)
            dfs(pac, r, 0, -1, heights)
        for c in range(C):
            dfs(pac, 0, c, -1, heights)
            dfs(atl, R-1, c, -1, heights)
        res = []
        for r in range(R):
            for c in range(C):
                if ((r, c) in atl and (r, c) in pac):
                    res.append([r, c])
        return res