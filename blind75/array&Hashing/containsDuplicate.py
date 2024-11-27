class Solution:
    def containsDuplicate(self, nums) -> bool:
        visit = {}
        for n in nums:
            if n in visit:
                return True
            visit[n] = True
        return False