def transposeMatrix(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    transposedMatrix = []
    for col in range(COLS):
        eachRow = []
        for row in range(ROWS):
            eachRow.append(matrix[row][col])
        transposedMatrix.append(eachRow)
    return transposedMatrix