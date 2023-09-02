def backspaceComp(s:str, t:str):
    newS, newT = [], []

    for i in s:
        if i == '#':
            if len(newS) > 0:
                newS.pop()
        else:
            newS.append(i)
    
    for i in t:
        if i == '#':
            if len(newT) > 0:
                newT.pop()
        else:
            newT.append(i)
    
    lenNewS, lenNewT = len(newS), len(newT)
    if lenNewS == lenNewT:
        for i in range(0, lenNewS):
            if newS[i] != newT[i]:
                return False
        return True
    return False

s = "hd#dp#czsp#####"
t = "hd#dp#czsp######"
print(backspaceComp(s, t))

def backspaceCompOptimal(s: str, t: str):
    i, j = len(s) - 1, len(t) - 1
    totalBackS = totalBackT = 0

    while i>=0 or j>=0:
        if i>=0 and j>=0:
            if s[i] != '#' and t[j] != '#' and totalBackS == 0 and totalBackT == 0:
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            else:
                if s[i] == '#':
                    totalBackS += 1
                    i-=1
                else:
                    if totalBackS:
                        totalBackS -=1
                        i-=1
                if t[j] == '#':
                    totalBackT += 1
                    j-=1
                else:
                    if totalBackT:
                        totalBackT -=1
                        j-=1
        else:
            if i>=0:
                if s[i] == '#':
                    totalBackS += 1
                    i-=1
                else:
                    if totalBackS:
                        totalBackS -=1
                        i-=1
                    else:
                        return False
            if j>=0:
                if t[j] == '#':
                    totalBackT += 1
                    j-=1
                else:
                    if totalBackT:
                        totalBackT -=1
                        j-=1
                    else:
                        return False
    return True

print(backspaceCompOptimal(s, t))