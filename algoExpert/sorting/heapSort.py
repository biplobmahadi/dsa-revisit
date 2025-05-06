def heapSort(array):
    heapify(array)
    for i in reversed(range(1, len(array))):
        swap(i, 0, array)
        shiftDown(0, i-1, array)
    return array

def heapify(arr):
    curr = (len(arr)-2)//2
    for i in reversed(range(curr+1)):
        shiftDown(i, len(arr)-1, arr)

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

def shiftDown(i, e, arr):
    l = i*2+1
    while l <= e:
        r = i*2+2
        if r <= e and arr[l] < arr[r] > arr[i]:
            swap(i, r, arr)
            i = r
        elif arr[i] < arr[l]:
            swap(i, l, arr)
            i = l
        else:
            break
        l = i*2+1
