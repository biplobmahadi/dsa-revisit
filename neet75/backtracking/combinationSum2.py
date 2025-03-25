class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        candidates.sort()
        def solve(i, cSum):
            if cSum == target:
                res.append(curr.copy())
                return
            if cSum > target:
                return
            j = i
            while j < len(candidates):
                cSum += candidates[j]
                curr.append(candidates[j])
                solve(j+1, cSum)
                cSum -= candidates[j]
                curr.pop()
                while j+1 < len(candidates) and candidates[j] == candidates[j+1]:
                    j+=1
                j+=1

        solve(0, 0)
        return res