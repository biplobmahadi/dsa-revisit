class Node:
    def __init__(self):
        self.child = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = Node()
            curr = curr.child[w]
        curr.isWord = True

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def dfs(r, c, node, res, board, s):
    if (r<0 or c<0 or r>=len(board) or c>=len(board[0]) or 
        board[r][c]=='#' or board[r][c] not in node.child): 
        return
    tmp = board[r][c]
    s+=tmp
    print(s)
    if node.child[tmp].isWord:
        res.add(s)
    board[r][c]='#'
    for nr, nc in directions:
        dfs(r+nr, c+nc, node.child[tmp], res, board, s)
    board[r][c]=tmp

def findWords(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    res = set()
    for r in range(len(board)):
        for c in range(len(board[0])):
            dfs(r, c, trie.root, res, board, '')
    return list(res)

print(findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))