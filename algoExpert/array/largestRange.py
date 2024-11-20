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
                