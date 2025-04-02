def powerset(array):
    res = []
    def solve(i, arr):
        if i == len(array):
            res.append(arr.copy())
            return 
        arr.append(array[i])
        solve(i+1, arr)
        arr.pop()
        solve(i+1, arr)
    solve(0, [])
    return res