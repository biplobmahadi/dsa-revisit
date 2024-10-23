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
    