def is_valid(s: str):
    stack, parenthesis = [], {'(': ')', '{': '}', '[': ']'}
    for i in s:
        if i in parenthesis:
            stack.append(i)
        else:
            if len(stack):
                popped = stack.pop()
                val = parenthesis.get(popped)
                if val != i:
                    return False
            else:
                return False
    
    return len(stack) == 0

s = "]"
print(is_valid(s))