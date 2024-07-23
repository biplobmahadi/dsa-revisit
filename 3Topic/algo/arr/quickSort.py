arr = [2, 5, 2, -1, 45, 0, 3, 43, 23]

def getPivot(arr, left, right):
    i, j, p = left, left, right
    while j < p:
        if arr[j] < arr[p]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i+=1
        j+=1
    tmp = arr[i]
    arr[i] = arr[p]
    arr[p] = tmp
    return i


def quick(arr, left, right):
    if left >= right:
        return
    pivotPosition = getPivot(arr, left, right)
    quick(arr, left, pivotPosition-1)
    quick(arr, pivotPosition+1, right)
    return arr

print(quick(arr, 0, len(arr)-1))
