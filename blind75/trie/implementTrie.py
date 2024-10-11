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

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.child:
                return False
            curr = curr.child[w]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.child:
                return False
            curr = curr.child[w]
        return True

trie = Trie();
trie.insert("apple");
print(trie.search("apple")   )# return True
print(trie.search("app")    )# return False
print(trie.startsWith("app") )# return True
trie.insert("app");
print(trie.search("app"))# return True