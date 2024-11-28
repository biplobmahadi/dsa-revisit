class Solution:
    def productExceptSelf(self, nums):
        res = []
        pre, post = 1, 1
        for n in nums:
            res.append(pre)
            pre *= n
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res