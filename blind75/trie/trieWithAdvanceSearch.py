class Node:
    def __init__(self):
        self.child = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = Node()
            curr = curr.child[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if len(word) == i:
                return curr.isWord
            if word[i] == '.':
                for val in curr.child.values():
                    if dfs(i+1, val):
                        return True
                return False
            if word[i] not in curr.child:
                return False
            return dfs(i+1, curr.child[word[i]])
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)