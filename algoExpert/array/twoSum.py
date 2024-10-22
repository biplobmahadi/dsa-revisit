def twoNumberSum(array, targetSum):
    map = {}
    for n in array:
        comp = targetSum - n
        if comp in map:
            return [comp, n]
        map[n] = True
    return []