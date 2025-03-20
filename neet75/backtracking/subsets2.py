class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        nums.sort()
        def solve(i):
            if i == len(nums):
                res.append(curr.copy())
                return 
            curr.append(nums[i])
            solve(i+1)
            curr.pop()
            while i+1<len(nums) and nums[i]== nums[i+1]:
                i+=1
            solve(i+1)
        solve(0)
        return res