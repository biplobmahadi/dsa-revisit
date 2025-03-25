class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        def solve(i):
            if i == len(nums):
                res.append(curr.copy())
                return 
            curr.append(nums[i])
            solve(i+1)
            curr.pop()
            solve(i+1)
        solve(0)
        return res