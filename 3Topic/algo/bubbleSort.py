arr = [2, 5, 2, -1, 45, 0, 3, 43, 23]


def swap(i, j, arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def bubble(arr):
    for i in range(0, len(arr)-1):
        for j in range(1, len(arr)-i):
            if arr[j] < arr[j-1]:
                swap(j, j-1, arr)
    return arr


print(bubble(arr))
