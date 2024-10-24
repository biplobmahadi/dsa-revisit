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
    