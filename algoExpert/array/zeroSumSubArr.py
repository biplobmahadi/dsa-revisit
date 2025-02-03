# O(n) time | O(n) space
def zeroSumSubarray(nums):
    sums = set([0])
    currSum = 0
    for num in nums:
        currSum += num
        if currSum in sums:
            return True
        sums.add(currSum)
    return False

def zeroSumSubarray2(nums):
    curr = 0
    prevSums = {0}
    for n in nums:
        curr+=n
        if curr in prevSums:
            return True
        prevSums.add(curr)
    return False
