def minCostClimbingStairs(cost):
    n = len(cost)
    return min(minCost(n-1, cost), minCost(n-2, cost))

def minCost(i, cost):
    if i < 0: return 0
    if i==0 or i==1: return cost[i]
    return cost[i] + min(minCost(i-1, cost), minCost(i-2, cost))

print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))