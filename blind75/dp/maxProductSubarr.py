class Solution:
    def maxProduct(self, nums) -> int:
        res = minP = maxP = nums[0]
        for i in range(1, len(nums)):
            p1 = minP * nums[i]
            p2 = maxP * nums[i]
            minP = min(p1, p2, nums[i])
            maxP = max(p1, p2, nums[i])
            res = max(minP, maxP, res)
        return res
