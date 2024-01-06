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