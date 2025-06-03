def bestDigits(number, numDigits):
    stack = []
    for curr in number:
        while numDigits and stack and stack[len(stack)-1] < curr:
            numDigits-=1
            stack.pop()
        stack.append(curr)
        
    while numDigits:
        stack.pop()
        numDigits-=1
        
    return ''.join(stack)
