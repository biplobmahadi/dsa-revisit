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
            if newS[i] is not newT[i]:
                return False
        return True
    return False

s = "a#c"
t = "b"
print(backspaceComp(s, t))