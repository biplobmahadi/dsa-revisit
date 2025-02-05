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


def sweetAndSavory2(dishes, target):
    sweet = sorted([n for n in dishes if n<0], key=abs)
    savory = sorted([n for n in dishes if n>0])
    res = [0, 0]
    near = float('inf')
    i, j = 0, 0
    while i < len(sweet) and j < len(savory):
        total = sweet[i] + savory[j]
        if total <= target:
            diff = target - total
            if diff < near:
                res = [sweet[i], savory[j]]
                near = diff
            j+=1
        else:
            i+=1        
    return res
            