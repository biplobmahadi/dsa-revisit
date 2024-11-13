# O(n(logn)) time | O(n) space
def sweetAndSavory(dishes, target):
    sweet = sorted([dish for dish in dishes if dish<0], key=abs)
    savory = sorted([dish for dish in dishes if dish>0])

    bestPair = [0, 0]
    bestDiff = float('inf')

    sweetInx, savoryInx = 0, 0
    while sweetInx < len(sweet) and savoryInx < len(savory):
        pair = sweet[sweetInx] + savory[savoryInx]

        if pair <= target:
            diff = target - pair
            if diff < bestDiff:
                bestDiff = diff
                bestPair = [sweet[sweetInx], savory[savoryInx]]
            savoryInx+=1
        else:
            sweetInx += 1
    return bestPair
