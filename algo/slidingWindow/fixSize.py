# given int arr, 
# return true if there are 2 elements within a window of size k that are equal

nums = [1, 2, 3, 2, 3, 4]

def bruteSliding(nums, k):
    for l in range(len(nums)):
        for r in range(l+1, min(l+k, len(nums))):
            if nums[l] == nums[r]:
                return True
    return False

# def optimalSliding(nums, k):
#     hashSet = set()
#     l = 0
#     for r in range(len(nums)):
#         if r - l + 1 > k:
#             hashSet.remove(nums[l])
#             l += 1
#         if nums[r] in hashSet:
#             return True
#         hashSet.add(nums[r])
#     return False

# print(bruteSliding(nums, 2))
# print(optimalSliding(nums, 2))
