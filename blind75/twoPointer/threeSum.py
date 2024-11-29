class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while r > l:
                total = nums[i] + nums[l] + nums[r]
                if total > 0: r-=1
                elif total < 0: l+=1
                else:
                    res.append([nums[i] , nums[l] , nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return res