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
    
