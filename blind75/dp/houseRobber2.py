class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.robbing(nums[1:]), self.robbing(nums[:-1]))

    def robbing(self, nums) -> int:
        dpOne, dpTwo = 0, nums[0]
        for i in range(1, len(nums)):
            dpOne, dpTwo = dpTwo, max(nums[i]+dpOne, dpTwo)
        return dpTwo