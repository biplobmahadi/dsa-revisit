import math

def reversePolishNotation(tokens):
    stack = []
    for n in tokens:
        if n not in '+-*/':
            stack.append(int(n))
            continue
        p2 = stack.pop()
        p1 = stack.pop()
        if n == '+':
            stack.append(p1+p2)
        elif n == '-':
            stack.append(p1-p2)
        elif n == '*':
            stack.append(p1*p2)
        else:
            stack.append(math.trunc(p1/p2))
    return stack[0]
        
