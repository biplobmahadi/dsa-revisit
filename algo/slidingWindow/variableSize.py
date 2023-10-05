# given int arr,
# find len of longest subarr, where same value in each position

nums = [1, 2, 2, 3, 3, 3]

def longestSubarr(nums):
    long, l = 0, 0
    for r in range(len(nums)):
        if nums[l] != nums[r]:
            l = r
        long = max(long, r-l+1)
    return long

print(longestSubarr(nums))