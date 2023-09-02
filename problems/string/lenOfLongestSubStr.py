def lenOfLongestSubStr(s):
    n, longest = len(s), 0
    for i in range(0, n):
        map = {}
        for j in range(i, n):
            if s[j] not in map:
                map[s[j]] = True
            else:
                break
        
        longest = max(longest, len(map))
    return longest

s = ' '
print(lenOfLongestSubStr(s))