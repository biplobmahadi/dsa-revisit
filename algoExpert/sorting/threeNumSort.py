def threeNumberSort(array, order):
    p = 0
    for curr in order:
        i = p
        while i < len(array):
            val = array[i]
            if val == curr:
                array[p], array[i] = array[i], array[p]
                p+=1
            i+=1
        
    return array
