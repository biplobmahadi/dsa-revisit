import math

def smallestDifference(arrayOne, arrayTwo):
    currentDiff = math.inf
    pair = [math.inf, math.inf]

    for one in arrayOne:
        for two in arrayTwo:
            distance = abs(one-two)
            if currentDiff > distance:
                currentDiff = distance
                pair = [one, two]
    return pair


def smallestDifference2(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    i, j = 0, 0
    currDiff, res = math.inf, [0, 0]

    while i < len(arrayOne) and j < len(arrayTwo):
        one, two = arrayOne[i], arrayTwo[j]
        distance = abs(one-two)
        if one<two:
            i+=1
        elif two<one:
            j+=1
        else: 
            return [one, two]
        if distance < currDiff:
            currDiff = distance
            res = [one, two]
    return res
    
def smallestDifference2(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    diff, res, i, j = float('inf'), [], 0, 0
    while i<len(arrayOne) and j<len(arrayTwo):
        curr = abs(arrayOne[i]-arrayTwo[j])
        if not curr: return [arrayOne[i], arrayTwo[j]]
        if curr < diff:
            diff = curr
            res = [arrayOne[i], arrayTwo[j]]
        if arrayOne[i] < arrayTwo[j]:
            i+=1
        else:
            j+=1
    return res
