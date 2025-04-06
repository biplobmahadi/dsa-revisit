def riverSizes(matrix):
    res = []
    def bfs(r, c):
        if matrix[r][c] == 0:
            return None
        q = []
        q.append((r, c))
        count = 0
        matrix[r][c] = 0
        while q:
            pr, pc = q.pop()
            count+=1
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in direction:
                nr, nc = pr+dr, pc+dc
                if nr>=0 and nc>=0 and nr<len(matrix) and nc<len(matrix[0]) and matrix[nr][nc] != 0:
                    q.append((nr, nc))
                    matrix[nr][nc] = 0
        return count
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            val = bfs(r, c)
            if val: res.append(val)
    return res
