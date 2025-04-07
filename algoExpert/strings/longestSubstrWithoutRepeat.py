def longestSubstringWithoutDuplication(string):
    visit = set()
    largest = 0
    res = [-1, -1]
    i, j = 0, 0
    while j<len(string):
        if string[j] not in visit:
            l = j-i+1
            if largest < l:
                largest = l
                res = [i, j]
            visit.add(string[j])
            j+=1
            continue
        while string[j] in visit:
            visit.remove(string[i])
            i+=1

    return string[res[0]: res[1]+1]
            
