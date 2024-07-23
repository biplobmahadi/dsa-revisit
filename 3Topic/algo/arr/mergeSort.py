arr = [2, 5, 2, -1, 45, 0, 3, 43, 23]

def merge(arr1, arr2):
    res, i, j = [], 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i+=1
        else: 
            res.append(arr2[j])
            j+=1
    if i < len(arr1):
        for k in range(i, len(arr1)):
            res.append(arr1[k])
    if j < len(arr2):
        for k in range(j, len(arr2)):
            res.append(arr2[k])
    return res

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    arr1 = arr[0: mid]
    arr2 = arr[mid: len(arr)]
    return merge(mergeSort(arr1), mergeSort(arr2))

print(mergeSort(arr))