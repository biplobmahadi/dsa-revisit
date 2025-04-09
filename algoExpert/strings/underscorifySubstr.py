def underscorifySubstring(string, substring):
    l = 0
    res = []
    for r in range(len(string)):
        s = string[l:r+1]
        if s == substring:
            res.append([l, r])
            l +=1
        else:
            if r-l+1 == len(substring):
                l +=1
    print(res)
    if not res:
        return string
    newRes = []
    prev = res[0]
    for i in range(1, len(res)):
        curr = res[i]
        if prev[1]+1 >= curr[0]:
            prev = [prev[0], curr[1]]
        else:
            newRes.append(prev)
            prev = curr
    newRes.append(prev)
    res1 = list(string)
    c = 0
    for i, (l, r) in enumerate(newRes):
        res1.insert(l+c, '_')
        c+=1
        res1.insert(r+1+c, '_')
        c+=1
    print(''.join(res1))
    return ''.join(res1)
