def minimumPassesOfMatrix(matrix):
    count = 0
    direction = [[1, 0], [0,1], [-1, 0], [0, -1]]
    def checkNegative():
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] < 0:
                    return -1
    while True:
        v = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] > 0:
                    for dr, dc in direction:
                        nr, nc = dr+r, dc+c
                        if nr>=0 and nc>=0 and nr<len(matrix) and nc < len(matrix[0]) and matrix[nr][nc]<0:
                            v.add((nr, nc))
        
        if not v:
            if checkNegative() == -1:
                return -1
            return count
        for r, c in v:
            matrix[r][c] *= -1
        count+=1

    

