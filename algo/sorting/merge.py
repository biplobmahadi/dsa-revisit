def merge(arr1, arr2):
    mergedArr = []
    i, j = 0, 0
    lenArr1, lenArr2 = len(arr1), len(arr2)
    while i < lenArr1 or j < lenArr2:
        if i < lenArr1 and j < lenArr2:
            if arr1[i] < arr2[j]:
                mergedArr.append(arr1[i])
                i+=1
            else:
                mergedArr.append(arr2[j])
                j+=1
        elif i < lenArr1:
            mergedArr.append(arr1[i])
            i+=1
        else:
            mergedArr.append(arr2[j])
            j+=1
    return mergedArr


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]

    return merge(mergeSort(arr1), mergeSort(arr2))

arr = [4, 3, 9, 5, 1, 8, 2, 10, 2, 3, 4, 5, 0]

print(mergeSort(arr))