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
        inc = rec(i+1, p, w, newC) + p[i]
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
        inc = recMemo(i+1, p, w, newC, cache) + p[i]
        cache[i][c] = max(inc, cache[i][c])
    return cache[i][c]

print(topDownMemo([4, 4, 7, 1], [5, 2, 3, 1], 8))
