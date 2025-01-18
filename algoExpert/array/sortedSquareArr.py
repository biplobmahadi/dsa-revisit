def sortedSquaredArray(array):
    res = [0] * len(array)
    left, right = 0, len(array)-1
    for i in reversed(range(len(array))):
        if abs(array[right]) > abs(array[left]):
            res[i] = array[right] * array[right]
            right -= 1
        else: 
            res[i] = array[left] * array[left]
            left += 1
    return res

def sortedSquaredArray(array):
    sqArr = []
    l, r = 0, len(array)-1
    while r>=l:
        if abs(array[l]) > abs(array[r]):
            sqArr.append(array[l] ** 2)
            l+=1
        else:
            sqArr.append(array[r] ** 2)
            r-=1
    sqArr.reverse()
    return sqArr
