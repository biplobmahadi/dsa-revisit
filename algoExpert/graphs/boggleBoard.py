class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False


class WordDict:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for s in word:
            if s not in curr.child:
                curr.child[s] = TrieNode()
            curr = curr.child[s]
        curr.isWord = True     


def boggleBoard(board, words):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    visit= set()
    res = set()
    def dfs(r, c, s, visit, wordDict):
        if (r<0 or c<0 or r>=len(board) or c >= len(board[0]) or (r, c) in visit or board[r][c] not in wordDict.child):
            return
        ch = board[r][c]
        s+=ch
        visit.add((r, c))
        if wordDict.child[ch].isWord:
            res.add(s)
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            dfs(nr, nc, s, visit, wordDict.child[ch])
        visit.remove((r,c))
        
    wordDict = WordDict()
    for w in words:
        wordDict.addWord(w)
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            dfs(r, c, '', visit, wordDict.root)

    
    return list(res)
