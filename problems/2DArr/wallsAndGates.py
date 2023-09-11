import math

matrix = [
  [math.inf, -1, 0, math.inf],
  [math.inf, math.inf, math.inf, -1],
  [math.inf, -1, math.inf, -1],
  [0, -1, math.inf, math.inf],
]
matrix2 = [
  [math.inf, -1, 0, math.inf],
  [-1, math.inf, math.inf, -1],
  [math.inf, -1, math.inf, -1],
  [0, -1, math.inf, math.inf],
]

def gatesAndWalls(matrix):
    if not (matrix and matrix[0]): return matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                dfs(matrix, row, col, 0)
    return matrix

def dfs(matrix, row, col, count):
    if (row<0 or col<0 or row>=len(matrix) or col>=len(matrix[0]) or 
        matrix[row][col]<count):
        return 
    matrix[row][col] = count
    dfs(matrix, row-1, col, count+1)
    dfs(matrix, row, col+1, count+1)
    dfs(matrix, row+1, col, count+1)
    dfs(matrix, row, col-1, count+1)

print(gatesAndWalls(matrix))
