import numpy as np
from readEquation import *

def sum (k, end, matrix, value):
    res = 0
    for i in range(1, end):
        res+=matrix[k][i]* value

    return res


def gaussSeidel(file_path, approx_error):
    matrix, vector = convertContentToArray(readfile(file_path))

    error=0
    n=matrix.size[0]
    result=[]

    while error < approx_error:

        for k in range(1, n):
            result[k]= (1/matrix[k][k])*(vector[k]-sum(k, n, matrix, )-sum(
                k,n,matrix,))






