def fiboIterative(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            res = a + b
            a = b
            b = res
        return res
    
print(fiboIterative(8))