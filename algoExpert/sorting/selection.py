def selectionSort(array):
    for i in range(len(array)):
        small = i
        for j in range(i+1, len(array)):
            if array[small] > array[j]:
                small = j
        if i != small:
            array[small], array[i] = array[i], array[small]
    return array
