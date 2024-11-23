class Solution:
    def rotate(self, matrix) -> None:
        if len(matrix) == 1: return

        t, b = 0, len(matrix)-1
        while t <= b:
            l, r = t, b
            for i in range(r-l):
                tmp = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = tmp
            t+=1
            b-=1
        