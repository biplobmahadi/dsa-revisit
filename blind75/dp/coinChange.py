import math

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        res = [math.inf]
        def goo(amount, total):
            if amount == 0: 
                res[0] = min(res[0], total)
            for coin in coins:
                if amount - coin >= 0:
                    goo(amount-coin, total+1)
        goo(amount, 0)
        return res[0] if res[0] is not math.inf else -1