def validIPAddresses(string):
    res = []
    for i in range(1, min(len(string), 4)):
        curr = ['', '', '', '']
        curr[0] = string[:i]
        if not isValid(curr[0]):
            continue
        for j in range(i+1, min(4+i, len(string))):
            curr[1] = string[i:j]
            if not isValid(curr[1]):
                continue
            for k in range(j+1, min(4+j, len(string))):
                curr[2] = string[j:k]
                curr[3] = string[k:]
                if isValid(curr[2]) and isValid(curr[3]):
                    res.append('.'.join(curr))
    return res

def isValid(s):
    intS = int(s)
    if intS > 255:
        return False
    return len(s) == len(str(intS))