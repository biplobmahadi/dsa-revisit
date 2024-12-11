from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums)-1, nums[0]
        while r>=l:
            m = (r+l) // 2
            res = min(res, nums[m])
            if nums[m] < nums[r]:
                r = m-1
            else:
                l = m+1
        return res
            