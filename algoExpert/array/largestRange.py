# O(2 * n) time | O(n) space
def largestRange(array):
    dataset = set(array)
    largest = 0
    res = []
    for n in array:
        if n-1 in dataset:
            continue
        curr = 0
        val = n
        while val in dataset:
            curr+=1
            val+=1
        if curr > largest:
            largest = curr
            res = [n, val-1]
    return res
                
def largestRange2(array):
    have = set(array)
    currMax = 0
    res = []
    for n in array:
        if n-1 not in have:
            curr = n
            currL = 0
            while curr in have:
                currL+=1
                curr+=1
            if currL > currMax:
                res = [n, curr-1]
                currMax = currL
    return res
