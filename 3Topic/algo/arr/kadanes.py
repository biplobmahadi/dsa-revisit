arr = [4, -1, 2, -7, 3, 4]
arr2 = [-4, -5, -1, -7, -8, -2]


def kadanes(arr):
    maxSum = arr[0]
    current = arr[0]

    for n in arr[1:]:
        current = max(current+n, n)
        maxSum = max(maxSum, current)
    return maxSum

print(kadanes(arr))
