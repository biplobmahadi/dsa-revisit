def bubbleSort(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(1, length - i):
            if arr[j-1] > arr[j]:
                tmp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = tmp
    return arr

arr = [4, 3, 9, 5, 1, 8, 2, 10, 2, 3, 4, 5, 0]
print(bubbleSort(arr))