# max profit in bagpack

# topDown
def topDown(profit, weight, capacity):
    return rec(0, profit, weight, capacity)

def rec(i, p, w, c):
    if i == len(p):
        return 0
    maxProfit = rec(i+1, p, w, c)
    newC = c - w[i]
    if newC >=0:
        inc = rec(i, p, w, newC) + p[i]
        maxProfit = max(inc, maxProfit)
    return maxProfit

print(topDown([4, 4, 7, 1], [5, 2, 3, 1], 8))

def topDownMemo(profit, weight, capacity):
    cache = [[-1] * (capacity+1) for _ in range(len(profit))]
    return recMemo(0, profit, weight, capacity, cache)

def recMemo(i, p, w, c, cache):
    if i == len(p):
        return 0
    if cache[i][c] != -1:
        return cache[i][c]
    
    cache[i][c] = recMemo(i+1, p, w, c, cache)
    newC = c - w[i]
    if newC >=0:
        inc = recMemo(i, p, w, newC, cache) + p[i]
        cache[i][c] = max(inc, cache[i][c])
    return cache[i][c]

print(topDownMemo([4, 4, 7, 1], [5, 2, 3, 1], 8))

def bottomUp(profit, weight, capacity):
    cache = [[0] * (capacity+1) for _ in range(len(profit))]

    for c in range(capacity+1):
        if c >= weight[0]:
            cache[0][c] = profit[0]
    for i in range(1, len(profit)):
        for c in range(1, capacity+1):
            skip = cache[i-1][c]
            inc = 0
            if c - weight[i] >= 0:
                inc = profit[i] + cache[i][c - weight[i]]
            cache[i][c] = max(skip, inc)
    return cache[len(profit)-1][capacity]

print(bottomUp([4, 4, 7, 1], [5, 2, 3, 1], 8))

def bottomUpOptimization(profit, weight, capacity):
    cache = [0] * (capacity+1)

    for i in range(len(profit)):
        newArr = [0] * (capacity+1)
        for c in range(capacity+1):
            skip = cache[c]
            inc = 0
            if c - weight[i] >= 0:
                inc = profit[i] + newArr[c - weight[i]]
            newArr[c] = max(skip, inc)
        cache = newArr
    return cache[capacity]

print(bottomUpOptimization([4, 4, 7, 1], [5, 2, 3, 1], 8))
