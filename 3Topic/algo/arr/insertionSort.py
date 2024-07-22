arr = [2, 5, 2, -1, 45, 0, 3, 43, 23]

def insertion(arr: list):
    for i in range(1, len(arr)):
        if arr[i] <= arr[0]:
            popped = arr.pop(i)
            arr.insert(0, popped)
        else:
            position = i
            for j in range(1, i):
                if arr[i] > arr[j-1] and arr[i] <= arr[j]:
                    position = j
            if position != i:
                popped = arr.pop(i)
                arr.insert(position, popped)

    return arr

print(insertion(arr))