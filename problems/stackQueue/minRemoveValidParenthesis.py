def minRemoveValidParenthesis(s: str):
    stack, map, newS = [], {}, ''
    for i, x in enumerate(s):
        if x == '(':
            stack.append(i)
            map[i] = True
        elif x == ')':
            if len(stack):
                popped = stack.pop()
                map[popped] = False
            else:
                map[i] = True
    for i, x in enumerate(s):
        if not map.get(i):
            newS += x
    return newS

s = 'ad'
print(minRemoveValidParenthesis(s))
