import numpy as np


def readfile(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content


def convertContentToArray(content):

    matrix_list = []
    vector = None
    state = None


    valid_states = {'A': matrix_list, 'b': 'vector'}

    for line in content:
        line = line.strip()

        if not line:
            continue

        if line.startswith('A:') or line.startswith('b:'):
            prefix = line.split(':')[0]
            if prefix in valid_states:
                if state == prefix:
                    raise ValueError(f"Duplicate '{prefix}:' encountered.")
                state = prefix
            else:
                raise ValueError(f"Unexpected prefix '{prefix}:' encountered.")
            continue

        numbers = np.array([float(x) for x in line.split()])
        if state == 'A':
            matrix_list.append(numbers)
        elif state == 'b':
            if vector is not None:
                raise ValueError("Duplicate 'b:' encountered.")
            vector = numbers

    if not matrix_list or vector is None:
        raise ValueError("File must contain both 'A:' and 'b:' sections.")

    matrix = np.vstack(matrix_list)
    rows, cols = matrix.shape


    if rows != len(vector) or any(cols != len(row) for row in matrix_list):
        raise ValueError("Inconsistent matrix and vector dimensions.")

    return matrix, vector


def print_output():
    try:
        matrix, vector = convertContentToArray(readfile('C:\\Users\\Admin\\Desktop\\uds zeinab\\eigene '
                          'Projekte\\Gauß-Seidel\\test\\brokenTxt\\vectorIsMissing.txt'  ))


        print("Matrix:")
        print(matrix)
        print("Vector:")
        print(vector)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    print_output()




