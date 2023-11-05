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
    """Returns True if matrices can be multiplied"""
    if len(matrix1[0]) == len(matrix2):
        return True
    else:
        return False


def matrix_multiplication(matrix1, matrix2):
    """Returns matrix representing arg1 multiplied by arg2"""
    result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return result_matrix


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
    result = matrix_multiplication(matrix1, matrix2)

    output_file = sys.argv[2]
    write_matrix_to_file(output_file, result)


main()
