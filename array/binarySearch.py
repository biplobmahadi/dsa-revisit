def findElForSortedArr(arr, element):
    low = 0
    high = len(arr) -1

    while high>=low:
        mid = (high + low )//2
        if arr[mid] == element: return mid
        if arr[mid] > element:
            high = mid -1
        else: low = mid + 1
    return -1

arr = [-3, -1, 0, 2, 4, 6, 7, 23, 43, 122]
print(findElForSortedArr(arr, 122))
