class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.word = True
    
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.word
        
    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return True

tr = Trie()
tr.insert('apple')
print(tr.search('dog'))
tr.insert('dog')
print(tr.search('dog'))
print(tr.startsWith('app'))
print(tr.search('app'))
tr.insert('app')
print(tr.search('app'))
