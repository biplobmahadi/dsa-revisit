def search(nums, target):
    l, r = 0, len(nums)-1

    while r>=l:
        m = (r+l)//2
        if nums[m] == target:
            return m
        if nums[m] > nums[r]:
            if target >= nums[l] and target < nums[m]:
                r = m - 1
            else: 
                l = m + 1
        else:
            if target > nums[m] and target <= nums[r]:
                l = m + 1
            else: 
                r = m - 1
        
    return -1

print(search([4,5,6,7,0,1,2], 0))