def exist(board, word) -> bool:
        def dfs(i, r, c):
            if i >= len(word): return True
            if (r<0 or c<0 or r>=len(board) or c>=len(board[0]) or
                board[r][c]=='#' or board[r][c]!=word[i]):
                return False
            tmp = board[r][c]
            board[r][c] = '#'
            res = (dfs(i+1, r+1, c) or dfs(i+1, r-1, c) or 
                    dfs(i+1, r, c+1) or dfs(i+1, r, c-1))
            board[r][c] = tmp
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(0, r, c):
                    return True
        return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
