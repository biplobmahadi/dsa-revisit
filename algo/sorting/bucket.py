arr = [2, 0, 1, 0, 2, 2]

def bucket(arr, num):
    bckt = [0]*num
    for n in arr:
        bckt[n] += 1
    p = 0
    for i, n in enumerate(bckt):
        for _ in range(n):
            arr[p] = i
            p += 1
    return arr

print(bucket(arr, 3))
