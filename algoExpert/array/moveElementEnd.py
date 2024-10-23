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
