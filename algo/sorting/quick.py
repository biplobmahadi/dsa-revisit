def getPivot(arr, left, right):
    i, j, pivot = left, left, right

    while pivot is not j:
        if arr[j] > arr[pivot]: 
            j+=1
        else:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i+=1
            j+=1
    tmp = arr[i]
    arr[i] = arr[pivot]
    arr[pivot] = tmp

    return i

def quickSort(arr, left, right):
    if left > right:
        return
    pivotPosition = getPivot(arr, left, right)
    quickSort(arr, left, pivotPosition-1)
    quickSort(arr, pivotPosition+1, right)
    return arr

arr = [2, 5, 34, 104, 1, 4, 0, 2, 9, 9, 3]
print(quickSort(arr, 0, len(arr)-1))
