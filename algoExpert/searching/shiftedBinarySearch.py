def shiftedBinarySearch(array, target):
    l, r = 0, len(array)-1
    while r>=l:
        m = (r+l)//2
        if array[m] == target:
            return m
        if array[m] < array[r]:
            # i m right
            if array[m]<target<=array[r]:
                l=m+1
            else:
                r=m-1
        else:
            # i am left
            if array[m]>target>=array[l]:
                r=m-1
            else:
                l=m+1
    return -1
