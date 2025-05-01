def quickSort(array):
    def solve(l, r):
        if l>=r: return
        p = getPivot(l, r)
        solve(l, p-1)
        solve(p+1, r)
        
    def getPivot(l, r):
        i = j = l
        p = r
        while j < p:
            if array[j] < array[p]:
                array[i], array[j] = array[j], array[i]
                i+=1
            j+=1
        array[i], array[p] = array[p], array[i]
        return i
    solve(0, len(array)-1)
    return array