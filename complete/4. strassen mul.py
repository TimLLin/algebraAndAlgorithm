import numpy as np
import math

z = 9
def make_matrix(matrix, n):
    closest_power_of_two = 2**(math.ceil(math.log(n, 2)))
    zeros = np.zeros((closest_power_of_two, closest_power_of_two))
    zeros[:matrix.shape[0], :matrix.shape[1]] = matrix
    return zeros

def divide_matrix(matrix):
    base = matrix.shape[0] // 2
    a11 = matrix[:base, :base]
    a12 = matrix[:base, base:]
    a21 = matrix[base:, :base]
    a22 = matrix[base:, base:]
    return a11, a12, a21, a22

def strassen(a, b):
    if len(a) == 1:
        return a * b

    a11, a12, a21, a22 = divide_matrix(a)
    b11, b12, b21, b22 = divide_matrix(b)

    m1 = strassen((a11+a22) % z, (b11+b22) % z)
    m2 = strassen((a21+a22) % z, b11 % z)
    m3 = strassen(a11 % z, (b12-b22) % z)
    m4 = strassen(a22 % z, (b21-b11) % z)
    m5 = strassen((a11+a12) % z, b22 % z)
    m6 = strassen((a21-a11) % z, (b11+b12) % z)
    m7 = strassen((a12-a22) % z, (b21+b22) % z)

    c11 = (m1 + m4 - m5 + m7) % z
    c12 = (m3 + m5) % z
    c21 = (m2 + m4) % z
    c22 = (m1 - m2 + m3 + m6) % z

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c

def fast_power(matrix, n):
    powers = []
    while n >= 1:
        if n % 2 == 0:
            powers.append(int(n))
            n /= 2
        else:
            powers.append(int(n))
            n -= 1
    powers = powers[::-1]

    matrix_powers = [matrix]
    for elem in range(1, len(powers)):
        if powers[elem] == powers[elem-1] * 2:

            matrix_powers.append(strassen(matrix_powers[elem-1], matrix_powers[elem-1]))
        elif powers[elem] == powers[elem-1] + 1:

            matrix_powers.append(strassen(matrix_powers[elem - 1], matrix_powers[0]))

    return matrix_powers[-1].astype('int64')

matrix = []
matrix.append(list(map(int, input().split())))
n = len(matrix[0])
for i in range(n-1):
    matrix.append(list(map(int, input().split())))
matrix = np.array(matrix)

if math.log(n, 2).is_integer() is False:
    matrix = make_matrix(matrix, n)

new_matrix = fast_power(matrix, n)
new_matrix = new_matrix[:n, :n]
answer = new_matrix.tolist()
for elem in answer:
    print(" ".join(map(str, elem)))