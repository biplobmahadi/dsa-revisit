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

def lenOfLongestSubStrOptimal(s):
    left, longest, map, n = 0, 0, {}, len(s)
    for right in range(0, n):
        current = s[right]
        seenInMap = map.get(current)
        if seenInMap is not None and seenInMap >= left:
            left = seenInMap + 1
        longest = max(longest, right - left + 1)
        map[current] = right
    return longest
print(lenOfLongestSubStrOptimal(s))