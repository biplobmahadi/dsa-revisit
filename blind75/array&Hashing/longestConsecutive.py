from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements, total = set(nums), 0
        for n in nums:
            if n-1 in elements:
                continue
            count = 1
            val = n
            while val+1 in elements:
                count+=1
                val += 1
            total = max(total, count)
        return total