def searchInSortedMatrix(matrix, target):
    r, c = 0, len(matrix[0])-1
    while r<len(matrix) and c>=0:
        if matrix[r][c] == target:
            return [r, c]
        elif matrix[r][c] > target:
            c-=1
        else:
            r+=1
    return [-1, -1]
