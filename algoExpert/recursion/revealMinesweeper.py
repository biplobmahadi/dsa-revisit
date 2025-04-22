def revealMinesweeper(board, row, column):
    if board[row][column] == 'M':
        board[row][column] = 'X'
        return board
    nei = getNei(row, column, board)
    c = 0
    for nr, nc in nei:
        if board[nr][nc] == 'M':
            c+=1
    if c>0:
        board[row][column] = str(c)
    else:
        board[row][column] = '0'
        for nr, nc in nei:
            if board[nr][nc] == 'H':
                revealMinesweeper(board, nr, nc)
    return board

def getNei(r, c, bo):
    dire = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    nei = []
    for dr, dc in dire:
        nr, nc = r+dr, c+dc
        if nr >=0 and nc>=0 and nr<len(bo) and nc < len(bo[0]):
            nei.append([nr, nc])
    return nei
