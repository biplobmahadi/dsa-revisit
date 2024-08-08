def charReplace(s, k):
    res = 0
    for i, n in enumerate(s):
        count = 0
        for j in range(i+1,len(s)):
            if count == k and s[j] != n:
                break
            if s[j] != n and count<k:
                count+=1
        res = max(res, j-i)
        
    return res

print(charReplace('ABAB', 2))
