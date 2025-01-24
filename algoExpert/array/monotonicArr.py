# O(n) time | O(1) space
def isMonotonic(array):
    isNonIncreasing = True
    isNonDecreasing = True

    for i in range(1, len(array)):
        firstElement, secondElement = array[i-1], array[i]
        if firstElement > secondElement:
            isNonDecreasing = False
        if firstElement < secondElement:
            isNonIncreasing = False

    return isNonIncreasing or isNonDecreasing
    
def isMonotonic2(array):
    if not array: return True
    isNonIn, isNonDe = False, False
    for i in range(1, len(array)):
        if array[i-1] == array[i]:
            continue
        if not isNonIn and not isNonDe:
            if array[i-1] < array[i]:
                isNonDe = True
            else:
                isNonIn = True
        if isNonIn and array[i-1] < array[i]:
            return False
        if isNonDe and array[i-1] > array[i]:
            return False
    return True