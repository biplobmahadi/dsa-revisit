def hasSingleCycle(array):
    total = 0
    i = 0
    while total < len(array):
        if total > 0 and i == 0:
            return False
        total += 1
        i = getI(i, array)
    return i == 0

def getI(i, array):
    jump = array[i]
    ni = (i + jump)%len(array)
    return ni if ni >= 0 else ni + len(array)
    
