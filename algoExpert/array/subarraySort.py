def subarraySort(array):
    def notOutside(inx):
        if inx == 0:
            return array[inx] > array[inx+1]
        if inx == len(array)-1:
            return array[inx] < array[inx-1]
        else:
            return array[inx] > array[inx+1] or array[inx] < array[inx-1]

    minIn, maxIn = float('inf'), float('-inf')
    for i in range(len(array)):
        if notOutside(i):
            minIn, maxIn = min(minIn, array[i]), max(maxIn, array[i])
    if minIn == float('inf'):
        return [-1, -1]
    left, right = 0, len(array)-1
    while minIn >= array[left]:
        left+=1
    while maxIn <= array[right]:
        right -=1
    return [left, right]

def notOutside(i, arr):
    if i == 0:
        return arr[i+1] < arr[i]
    if i == len(arr)-1:
        return arr[i-1] > arr[i]
    return arr[i-1] > arr[i] or arr[i+1] < arr[i]
    
def subarraySort2(array):
    minVal, maxVal = float('inf'), float('-inf')
    for i in range(len(array)):
        if notOutside(i, array):
            minVal, maxVal = min(minVal, array[i]), max(maxVal, array[i])

    if minVal == float('inf'):
        return [-1, -1]
    l, r = 0, len(array)-1
    while array[l] <= minVal:
        l+=1
    while array[r] >= maxVal:
        r-=1
    return [l, r]
