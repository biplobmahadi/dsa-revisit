def factorialIterative(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res

print(factorialIterative(5))


def facRecursive(n):
    if n <= 1:
        return 1
    return n * facRecursive(n-1)

print(facRecursive(5))