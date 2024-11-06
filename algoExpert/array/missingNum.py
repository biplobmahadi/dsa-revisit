# O(n) time | O(n) space
def missingNumbers(nums):
    res = []
    numSet = set(nums)
    for i in range(1, len(nums)+3):
        if i not in numSet:
            res.append(i)
    return res


# O(n) time | O(1) space
def missingNumbersOptimal(nums):
    numsSum = sum(nums)
    total = sum(range(1, len(nums)+3))
    missingTotal = total - numsSum
    avg = missingTotal // 2
    expectedRight = sum(range(avg+1, len(nums)+3))
    expectedLeft = sum(range(1, avg+1))
    leftSum = 0
    rightSum = 0
    for num in nums:
        if num <= avg:
            leftSum += num
        else: 
            rightSum += num
    return [expectedLeft-leftSum, expectedRight-rightSum]
