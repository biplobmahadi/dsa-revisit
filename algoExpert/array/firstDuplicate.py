# O(n) time | O(1) space
def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        mutateIdx = absValue - 1
        if array[mutateIdx] < 0:
            return absValue
        array[mutateIdx] *= -1
    return -1

def firstDuplicateValue(array):
    map = set()
    for n in array:
        if n in map:
            return n
        map.add(n)
    return -1