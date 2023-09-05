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

s = '(le(et(co(de)'
print(minRemoveValidParenthesis(s))

def minRemoveValidParenthesisGood(s: str):
    stack, arr = [], list(s)
    for i, x in enumerate(s):
        if x == '(':
            stack.append(i)
        elif x == ')':
            if len(stack):
                stack.pop()
            else:
                arr[i] = ''
    while len(stack):
        arr[stack.pop()] = ''
    return ''.join(arr)

print(minRemoveValidParenthesisGood(s))