from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                res = max(res, prices[j]-prices[i])
            else:
                i = j
        return res