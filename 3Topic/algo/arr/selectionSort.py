arr = [2, 5, 2, -1, 45, 0, 3, 43, 23]

def selection(arr):
    for i in range(0, len(arr)):
        small = i
        for j in range(i+1, len(arr)):
            if arr[small] > arr[j]:
                small = j
        tmp = arr[i]
        arr[i] = arr[small]
        arr[small] = tmp
    
    return arr

print(selection(arr))