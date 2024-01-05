# count the num of unique path from topleft to bottomright
# of a matrix, only can move right and down

def brute(r, c, row, col):
    if r == row or c == col:
        return 0
    if r == row-1 and c == col-1:
        return 1
    return brute(r+1, c, row, col) + brute(r, c+1, row, col)

print(brute(0, 0, 4, 4))

def memo(r, c, row, col, cache):
    if r == row or c == col:
        return 0
    if r == row-1 and c == col-1:
        return 1
    if cache[r][c] > 0:
        return cache[r][c]
    cache[r][c] = memo(r+1, c, row, col, cache) + memo(r, c+1, row, col, cache)
    return cache[r][c]

print(memo(0, 0, 4, 4, [[0]*4 for _ in range(4)]))


