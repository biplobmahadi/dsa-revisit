
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkBox(r, c):
            visit = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if board[i][j] != '.':
                        if board[i][j] in visit:
                            return True
                        visit.add(board[i][j])

        for i in range(9):
            visit = {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in visit:
                        return False
                    visit[board[i][j]] = True
        for i in range(9):
            visit2 = {}
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in visit2:
                        return False
                    visit2[board[j][i]] = True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if checkBox(i, j):
                    return False
        
        return True
        
