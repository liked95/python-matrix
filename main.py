# import openpyxl from 'openpyxl'

# 1. Swap function to swap row i and j from the given matrix
def swap( matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]
    return matrix


matrix = [[1,2,3], ['a', 'b', 'c'], [4, 5, 6]]

print('result', swap(matrix, 0, 2))

# 2. Scale function to multiple a row by certain number
def scale(matrix, i, j):
    # Loop through each element (or column) in the ith row and multiple it by j
    for column in range(len(matrix[i])):
        matrix[i][column] *= j
    return matrix

matrix2 = [[1,2,3], [8, 10, 22], [4, 5, 6]]

# 3. Combine function to multiple the content of ith row by k and add the result to row j
def row_combine(matrix, i, j, k):
    # Create an empty array to store value of row i * k
    array = []
    for col in range(len(matrix[i])):
        array.append(matrix[i][col]* k)
    
    # Loop row j and increment each col by the corresponding col from the newly created array
    for col in range(len(array)):
        matrix[j][col] += array[col]
    
    return matrix

    
print(row_combine(matrix2, 0, 2, 10))