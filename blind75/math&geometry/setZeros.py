class Solution:
    def setZeroes(self, matrix) -> None:
        firstRow = False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        firstRow = True
                    else:
                        matrix[r][0] = 0

        for r in reversed(range(len(matrix))):
            for c in reversed(range(len(matrix[0]))):
                if r != 0 and (matrix[0][c] == 0 or matrix[r][0] == 0):
                    matrix[r][c] = 0
        if firstRow:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        