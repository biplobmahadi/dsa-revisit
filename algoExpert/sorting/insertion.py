def insertionSort(array):
    for i in range(1, len(array)):
        for j in reversed(range(i)):
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]
    return array
