from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        def findKey(s):
            key = [0]*26
            for w in s:
                pos = ord(w) - ord('a')
                key[pos] += 1
            return tuple(key)
        for s in strs:
            key = findKey(s)
            anagrams[key].append(s)
        return list(anagrams.values())