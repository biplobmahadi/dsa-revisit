# O(n) time | O(n) space
def missingNumbers(nums):
    res = []
    numSet = set(nums)
    for i in range(1, len(nums)+3):
        if i not in numSet:
            res.append(i)
    return res
