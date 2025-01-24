class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 1
        res = [max(nums[:k])]
        for r in range(k, len(nums)):
            ans = max(nums[l:r+1])
            res.append(ans)
            l+=1
        return res

class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l, r = 0, 0
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            if r - k+1 >= 0:
                res.append(nums[q[0]])
                if q[0] == l:
                    q.popleft()
                l+=1
            r+=1
        return res