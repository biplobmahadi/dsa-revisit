def reverseStr(str):
    s = ''
    for i in range(len(str) -1, -1, -1):
        s += str[i]
    return s
    # return str[::-1]
    # can use list also 
    # and many more ways. also recursion
    # maybe space can be O(1), not sure

print(reverseStr('I am Biplob!'))
