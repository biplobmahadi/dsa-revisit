def binarySearch(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def searchRange(nums, target):
    if not nums:
        return [-1, -1]
    elPosition = binarySearch(nums, 0, len(nums)-1, target)
    if elPosition == -1:
        return [-1, -1]
    
    elPositionLeft = elPositionLeftPrev = elPositionRight = elPositionRightPrev = elPosition
    
    while elPositionLeft != -1:
        elPositionLeftPrev = elPositionLeft
        elPositionLeft = binarySearch(nums, 0, elPositionLeft - 1, target)
        
    while elPositionRight != -1:
        elPositionRightPrev = elPositionRight
        elPositionRight = binarySearch(nums, elPositionRight + 1, len(nums)-1, target)
    return [elPositionLeftPrev, elPositionRightPrev]

nums = [1, 1,1 , 1, 1, 1]
target = 1
print(searchRange(nums, target))