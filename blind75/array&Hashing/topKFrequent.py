class Solution:
    def topKFrequent(self, nums, k: int):
        elements = {}
        for n in nums:
            elements[n] = elements.get(n, 0) + 1
        bucket = [[] for _ in range(len(nums)+1)]
        for key, val in elements.items():
            bucket[val].append(key)
        res = []
        for num in reversed(bucket):
            res += num
            if k == len(res):
                return res