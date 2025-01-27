def spiralTraverse(array):
    res = []
    top, bottom, left, right = 0, len(array)-1, 0, len(array[0])-1
    
    while left <= right and top <= bottom:
        for i in range(left, right+1):
            res.append(array[top][i])
        top+=1
        for i in range(top, bottom+1):
            res.append(array[i][right])
        right-=1

        if left > right or bottom < top: break
        
        for i in range(right, left-1, -1):
            res.append(array[bottom][i])
        bottom-=1
        for i in range(bottom, top-1, -1):
            res.append(array[i][left])
        left+=1
        
    return res

def spiralTraverse2(array):
    t, b, l, r = 0, len(array)-1, 0, len(array[0])-1
    res = []
    while r>=l and b>=t:
        for i in range(l, r+1):
            res.append(array[t][i])
        t+=1
        for i in range(t, b+1):
            res.append(array[i][r])
        r-=1
        if b<t or r<l:
            break
        for i in range(r, l-1, -1):
            res.append(array[b][i])
        b-=1
        for i in range(b, t-1, -1):
            res.append(array[i][l])
        l+=1
    return res