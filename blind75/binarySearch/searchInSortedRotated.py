from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while r >= l:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[m] > nums[r]:
                # i m left sorted
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                # i m at right sorted
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1