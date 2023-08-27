def insertionSort(arr):
    length = len(arr)
    for i in range(1, length):
        el = arr[i]
        if el <= arr[0]:
            popped = arr.pop(i)
            arr.insert(0, popped)
        else:
            position = None
            for j in range(1, i):
                if arr[j-1] <= el and arr[j] >= el:
                    position = j
            if position:
                popped = arr.pop(i)
                arr.insert(position, popped)
    return arr

arr = [5, 12, 222, 3, 5, 34, 2, 6, 97, 2, 8, 1, 0, 7, 0]

print(insertionSort(arr))