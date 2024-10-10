def combinationSum(candidates, target):
        res = []
        ans = []
        def dfs(ii, total):
            if total == target:
                cloned = ans.copy()
                res.append(cloned)
                return
            if total > target: return
            for i in range(ii, len(candidates)):
                ans.append(candidates[i])
                total += candidates[i]
                dfs(i, total)
                ans.pop()
                total -= candidates[i]
        dfs(0, 0)
        return res

print(combinationSum([2,3,5], 8))