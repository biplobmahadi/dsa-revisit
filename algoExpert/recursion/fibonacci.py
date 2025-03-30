def getNthFib(n):
    if n == 1: return 0
    if n == 2: return 1
    n1 = 0
    n2 = 1
    for i in range(3, n+1):
        n3 = n1+n2
        n1= n2
        n2 = n3
    return n2