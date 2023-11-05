import sys


def read_matrixes_from_file(file_name):
    """Returns 2 matrices written in arg1"""
    matrix1 = []
    matrix2 = []
    cur_matrix = matrix1
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(x) for x in line.split()]
            if row == []:
                cur_matrix = matrix2
                continue
            cur_matrix.append(row)
    return matrix1, matrix2


def is_size_correct(matrix1, matrix2):
    """Returns True if 2nd matrix is not bigger than 1st one"""
    if (len(matrix1) <= len(matrix2)) and (len(matrix1[0]) <= len(matrix2[0])):
        return True
    else:
        return False


def matrix_convolution(matrix1, matrix2):
    """1st matrix's (arg1) convolution with 2nd matrix (arg2) as a kernel"""
    matrix_x = len(matrix1[0]) - len(matrix2[0]) + 1
    matrix_y = len(matrix1) - len(matrix2) + 1
    result = [[0 for _ in range(matrix_x)] for _ in range(matrix_y)]
    for x in range(matrix_x):
        for y in range(matrix_y):
            result[y][x] = cell_convolution(matrix1, matrix2, x, y)
    return result


def cell_convolution(matrix1, matrix2, shift_x, shift_y):
    """Returns convolution for cell with given shift"""
    result = 0
    for y in range(len(matrix2)):
        for x in range(len(matrix2[0])):
            result += matrix1[y+shift_y][x+shift_x] * matrix2[y][x]
    return result


def write_matrix_to_file(file_name, matrix):
    """Writes matrix (arg2) to file (arg1)"""
    with open(file_name, 'w') as file:
        for line in matrix:
            for num in line:
                file.write(str(num))
                file.write(" ")
            file.write("\n")


def main():
    input_file = sys.argv[1]
    matrix1, matrix2 = read_matrixes_from_file(input_file)
    if not(is_size_correct(matrix1, matrix2)):
        return
    result = matrix_convolution(matrix1, matrix2)
    write_matrix_to_file("output.txt", result)


main()
