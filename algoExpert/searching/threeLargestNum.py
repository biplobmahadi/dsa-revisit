def findThreeLargestNumbers(array):
    def shiftIndex(i, val):
        for j in range(i+1):
            if i == j:
                res[j] = val
            else:
                res[j] = res[j+1]

    res = [None, None, None]
    for n in array:
        if res[2] is None or n > res[2]:
            shiftIndex(2, n)
        elif res[1] is None or n > res[1]:
            shiftIndex(1, n)
        elif res[0] is None or n > res[0]:
            shiftIndex(0, n)
    
    return res