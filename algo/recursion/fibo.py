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
    
print(fiboIterative(10))
i = 0
j = 0
def fiboRecursive(n):
    global i
    i+=1
    if n < 2: return n
    return fiboRecursive(n-1) + fiboRecursive(n-2)

print(fiboRecursive(30))

def memoFib():
    cache = {}
    def fib(n):
        global j
        j+=1
        if n<2: return n
        if not cache.get(n):
            cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return fib

fib = memoFib()
print(fib(30))
print(i, j)