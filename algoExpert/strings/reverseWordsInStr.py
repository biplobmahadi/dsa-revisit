def reverseWordsInString(string):
    res = ''
    i = len(string)-1
    while i >=0:
        j = i
        while i>=0 and string[i] != ' ':
            i-=1
        word = string[i+1: j+1]
        res += word
        while i>=0 and string[i] == ' ':
            res+= ' '
            i-=1

    return res
