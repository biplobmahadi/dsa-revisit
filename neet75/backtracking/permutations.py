class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(i):
            if i == len(nums):
                return [[]]
            gotRes = solve(i+1)
            newRes = []
            for n in gotRes:
                for j in range(0, len(n)+1):
                    cp = n.copy()
                    cp.insert(j, nums[i])
                    newRes.append(cp)
            return newRes
        return solve(0)