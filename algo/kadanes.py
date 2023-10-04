# prob: given an int arr, find the largest sum of subarr

nums = [4, -1, 2, -7, 3, 4]

def brute(nums):
    maxSum = nums[0]
    for i in range(len(nums)):
        current = 0
        for j in range(i, len(nums)):
            current += nums[j]
            maxSum = max(maxSum, current)
    return maxSum

print(brute(nums))

def kadanes(nums):
    maxSum = nums[0]
    current = 0
    for n in nums:
        current += n
        current = max(current, 0)
        maxSum = max(maxSum, current)
    return maxSum

print(kadanes(nums))