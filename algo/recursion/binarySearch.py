def binarySearch(arr, l, r, val):
    if l>r:
        return -1
    mid = (l + r) // 2
    if arr[mid] == val:
        return mid
    elif arr[mid] > val:
        return binarySearch(arr, l, mid-1, val)
    else:
        return binarySearch(arr, mid+1, r, val)

arr = [1, 4, 5, 7, 9, 12, 45]
print(binarySearch(arr, 0, len(arr)-1, 1))