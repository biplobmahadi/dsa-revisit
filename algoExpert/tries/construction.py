# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            curr = self.root
            for j in range(i, len(string)):
                s = string[j]
                if s not in curr:
                    curr[s] = {}
                curr = curr[s]
            curr[self.endSymbol] = True

    def contains(self, string):
        curr = self.root
        for s in string:
            if s not in curr:
                return False
            curr = curr[s]
        return self.endSymbol in curr
