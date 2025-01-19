def transposeMatrix(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    transposedMatrix = []
    for col in range(COLS):
        eachRow = []
        for row in range(ROWS):
            eachRow.append(matrix[row][col])
        transposedMatrix.append(eachRow)
    return transposedMatrix

def transposeMatrix2(matrix):
    res = []
    R, C = len(matrix), len(matrix[0])
    for i in range(C):
        newArr = []
        for j in range(R):
            newArr.append(matrix[j][i])
        res.append(newArr)
    return res