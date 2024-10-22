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