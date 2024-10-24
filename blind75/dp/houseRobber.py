class Solution:
    def rob(self, nums) -> int:
        dp = {}
        def robbing(i):
            if i < 0: return 0
            if i not in dp:
                dp[i] = max(nums[i]+robbing(i-2), robbing(i-1))
            return dp[i]
        return robbing(len(nums)-1)

class Solution:
    def rob(self, nums) -> int:
        dpOne, dpTwo = 0, nums[0]
        for i in range(1, len(nums)):
            dpOne, dpTwo = dpTwo, max(nums[i]+dpOne, dpTwo)
        return dpTwo