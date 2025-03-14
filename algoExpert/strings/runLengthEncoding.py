def runLengthEncoding(string):
    res = ''
    i = 0
    while i < len(string):
        s = string[i]
        count = 1
        i+=1
        while i < len(string) and s == string[i]:
            count += 1
            i+=1
            if count == 9:
                res += '9'+s
                break
        if count<9:
            res+=str(count)+s
    return res
