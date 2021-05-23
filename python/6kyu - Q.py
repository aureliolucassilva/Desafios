# Link -> https://www.codewars.com/kata/52fba2a9adcd10b34300094c
def transpose(matrix):
    idxA = 0
    idxB = 0
    newMatrix = []
    matrixSample = []
    while idxB != len(matrix[0]):
        while idxA != len(matrix):
            matrixSample.append(matrix[idxA][idxB])
            idxA += 1
        newMatrix.append(matrixSample)
        matrixSample = []
        idxB += 1
        idxA -= len(matrix)
    return newMatrix
