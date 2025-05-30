def firstNonRepeatingCharacter(string):
    map = {}
    for s in string:
        map[s] = map.get(s, 0)+1
    for i, s in enumerate(string):
        if map[s] == 1:
            return i
    return -1
