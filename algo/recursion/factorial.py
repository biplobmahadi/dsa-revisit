def factorialIterative(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res

print(factorialIterative(5))