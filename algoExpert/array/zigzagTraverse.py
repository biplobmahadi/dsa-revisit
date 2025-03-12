def zigzagTraverse(array):
    res, r, c = [], 0, 0
    R, C = len(array), len(array[0])
    while r < R and c < C:
        res.append(array[r][c])
        if r == R-1 and c== C-1:
            break
        if r < R-1:
            r+=1
        else:
            c+=1
        while r>0 and c<C-1:
            res.append(array[r][c])
            r-=1
            c+=1
        res.append(array[r][c])
        if r==0 and c<C-1:
            c+=1
        else:
            r+=1
        while r<R-1 and c>0:
            res.append(array[r][c])
            r+=1
            c-=1
    return res
