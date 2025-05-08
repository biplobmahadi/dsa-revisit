def radixSort(array):
    if not array: return []
    digit = 0
    maxNum = max(array)
    while (maxNum / (10**digit)) > 0:
        countingSort(array, digit)
        digit+=1
    return array

def countingSort(arr, digit):
    sorted, count = [0]*len(arr), [0]*10
    for n in arr:
        dI = (n // (10**digit))%10
        count[dI] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(len(arr)-1, -1, -1):
        curr = arr[i]
        cdi = (curr // (10**digit))%10
        count[cdi] -= 1
        ind = count[cdi]
        sorted[ind] = curr
    for i in range(len(sorted)):
        arr[i] = sorted[i]
    


    
