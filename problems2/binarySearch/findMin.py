def findMin(nums):
    l, r, ans = 0, len(nums)-1, nums[0]

    while r >= l:
        m = (r + l) // 2
        ans = min(ans, nums[m])
        if nums[m] >= nums[r]:
            l = m + 1
        else:
            r = m - 1
    return ans

print(findMin([11,13,15,17]))
