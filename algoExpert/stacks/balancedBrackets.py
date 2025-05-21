def balancedBrackets(string):
    brackets = {'{': '}', '(': ')', '[': ']'}
    avail = ['(', ')', '[', ']', '{', '}']
    stack = []
    for n in string:
        if n not in avail:
            continue
        if n not in brackets:
            if not stack:
                return False
            p = stack.pop()
            if n != p:
                return False
        else:
            stack.append(brackets[n])

    return len(stack) == 0
 