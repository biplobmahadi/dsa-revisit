arr = [1, 0, 5, 2, 1, 0, 2, 1]


def bucket(arr, maxVal):
    buck = [0] * (maxVal+1)
    for n in arr:
        buck[n] += 1
    p = 0
    for i, n in enumerate(buck):
        for _ in range(n):
            arr[p] = i
            p+=1
    return arr

print(bucket(arr, 5))
