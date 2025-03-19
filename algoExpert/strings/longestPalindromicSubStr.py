def longestPalindromicSubstring(string):
    ln, res = 0, [-1, -1]
    for i in range(len(string)):
        l, r = i, i
        while l>=0 and r<len(string) and string[l] == string[r]:
            d = r-l+1
            if d > ln:
                ln = d
                res = [l, r]
            l-=1
            r+=1
        l, r = i, i+1
        while l>=0 and r<len(string) and string[l] == string[r]:
            d = r-l+1
            if d > ln:
                ln = d
                res = [l, r]
            l-=1
            r+=1
    return string[res[0]: res[1]+1]
    