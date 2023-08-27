def selectionSort(arr):
    length = len(arr)
    for i in range(0, length):
        small = i
        for j in range(i+1, length):
            if arr[small] > arr[j]:
                small = j
        
        if small is not i:
            tmp = arr[i]
            arr[i] = arr[small]
            arr[small] = tmp
    return arr

arr = [4, 3, 9, 5, 1, 8, 2, 10, 2, 3, 4, 5, 0]
print(selectionSort(arr))