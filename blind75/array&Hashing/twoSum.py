class Solution:
    def twoSum(self, nums, target: int):
        compSet = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in compSet:
                return [i, compSet[comp]]
            compSet[n] = i