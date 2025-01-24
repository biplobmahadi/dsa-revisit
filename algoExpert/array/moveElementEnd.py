# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    left, right = 0, len(array)-1

    while left < right:
        if array[right] == toMove:
            right -= 1
            continue
        if array[left] == toMove:
            tmp = array[left]
            array[left] = array[right]
            array[right] = tmp
            right -= 1
        left+=1
    return array

def moveElementToEnd2(array, toMove):
    r = len(array)-1
    for l in range(r, -1, -1):
        if array[r] == toMove:
            r -= 1
            continue
        if array[l] == toMove:
            array[r], array[l] = array[l], array[r]
            r -= 1
    return array