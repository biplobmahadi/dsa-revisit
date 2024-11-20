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
    