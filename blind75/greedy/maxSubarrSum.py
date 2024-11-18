class Solution:
    def maxSubArray(self, nums) -> int:
        res = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            curr += nums[i]
            curr = max(curr, nums[i])
            res = max(res, curr)
        return res
