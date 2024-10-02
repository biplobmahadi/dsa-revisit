res = [0]
def solve(profit, weight, capa, c, p, i):
    if capa < c or len(profit)-1 == i: return 0
    np1 = p + solve(profit, weight, capa, capa-weight[i], p+profit[i], i+1)
    np2 = p + solve(profit, weight, capa, capa, p, i+1)
    res[0] = max(np1, np2)
    return res[0]

solve([4, 4, 7, 1], [5, 2, 3, 1], 8, 8, 0, 0)
print(res)