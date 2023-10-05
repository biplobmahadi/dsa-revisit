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

# given positive int arr, 
# find min len subarr, where sum is greater or equal to target

def minLenSubarr(nums, target):
    total, lenght, l = 0, len(nums), 0
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            lenght = min(lenght, r-l+1)
            total -= nums[l]
            l += 1
    return lenght

arr = [2, 3, 1, 2, 4, 3]
print(minLenSubarr(arr, 6))