def mergeTwoSorted(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    if len1 == 0: return arr2
    if len2 == 0: return arr1

    i, j, newArr = 0, 0, []

    while i < len1 or j < len2 :
        if i < len1 and j < len2:
            if arr1[i] > arr2[j]:
                newArr.append(arr2[j])
                j+=1
            else:
                newArr.append(arr1[i])
                i+=1
        elif j < len2:
            newArr.append(arr2[j])
            j+=1
        else: 
            newArr.append(arr1[i])
            i+=1
            
    return newArr


arr1 = [5, 7, 12, 32, 43]
arr2 = [2, 4, 6]
print(mergeTwoSorted(arr1, arr2)) # O(m+n), O(m+n)


def merged(arr1, arr2):
    arr3: list = arr1 + arr2
    arr3.sort() # O(m+n log(m+n)), O(m+n)
    return arr3

print(merged(arr1, arr2))