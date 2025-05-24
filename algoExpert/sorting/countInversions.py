def mergeSort(array, res):
    if len(array) == 1:
        return array
    m = len(array)//2
    left = array[:m]
    right = array[m:]
    return merge(mergeSort(left, res), mergeSort(right, res), res)

def merge(arr1, arr2, resF):
    i, j = 0, 0
    res = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i]>arr2[j]:
            res.append(arr2[j])
            resF[0] += len(arr1) - i
            j+=1
        else:
            res.append(arr1[i])
            i+=1
    while i<len(arr1):
        res.append(arr1[i])
        i+=1
    while j<len(arr2):
        res.append(arr2[j])
        j+=1
    return res


def countInversions(array):
    if not array: return 0
    res = [0]
    mergeSort(array, res)
    return res[0]
