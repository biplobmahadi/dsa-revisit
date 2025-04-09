def removeIslands(matrix):
    for i in range(len(matrix)):
        dfs(matrix, i, 0)
        dfs(matrix, i, len(matrix[0])-1)
    for i in range(len(matrix[0])):
        dfs(matrix, 0, i)
        dfs(matrix, len(matrix)-1, i)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:
                matrix[r][c] = 0
            elif matrix[r][c] == 2:
                matrix[r][c] = 1
    return matrix

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def dfs(matrix, r, c):
    if matrix[r][c] == 0:
        return 
    matrix[r][c] = 2
    for dr, dc in directions:
        nr = r+dr
        nc = c+dc
        if nr >=0 and nc>=0 and nr<len(matrix) and nc< len(matrix[0]) and matrix[nr][nc] != 2:
            dfs(matrix, nr, nc)
