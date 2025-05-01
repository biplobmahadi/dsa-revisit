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


def threeNumberSortOptimal(array, order):
    i, f, l = 0, 0, len(array)-1
    while i <= l:
        if array[i] == order[0]:
            array[i], array[f] = array[f], array[i]
            f+=1
            i+=1
        elif array[i] == order[2]:
            array[i], array[l] = array[l], array[i]
            l-=1
        else:
            i+=1
    return array
