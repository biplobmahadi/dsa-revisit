def binarySearch(array, target):
    i, j = 0, len(array)-1
    while j>=i:
        m = (i+j)//2
        if array[m] == target:
            return m
        elif array[m] > target:
            j = m-1
        else: 
            i = m+1
    return -1
