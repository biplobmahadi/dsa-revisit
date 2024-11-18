class Solution:
    def canJump(self, nums) -> bool:
        target = len(nums)-1
        for i in reversed(range(len(nums)-1)):
            if i + nums[i] >= target:
                target = i
        return target == 0