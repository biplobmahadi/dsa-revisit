class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 1
        res = [max(nums[:k])]
        for r in range(k, len(nums)):
            ans = max(nums[l:r+1])
            res.append(ans)
            l+=1
        return res