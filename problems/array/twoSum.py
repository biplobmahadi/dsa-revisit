def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [3,2,4]
target = 6
print(twoSum(nums, target))

def twoSumOptimal(nums, target):
    map = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in map:
            return [i, map[complement]]
        map[x] = i

print(twoSumOptimal(nums, target))
