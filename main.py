import numpy as np
import math
import sys
sys.setrecursionlimit(10000)

z = 2
def make_matrix(matrix, n):
    closest_power_of_two = 2**(math.ceil(math.log(n, 2)))
    eye = np.eye(closest_power_of_two)
    eye[:matrix.shape[0], :matrix.shape[1]] = matrix
    return eye

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

def reverse(matrix):
    if len(matrix) == 1:
        return matrix
    base = matrix.shape[0] // 2
    b = matrix[:base, base:]
    c = matrix[base:, base:]
    d = matrix[:base, :base]
    c_r = reverse(c)
    d_r = reverse(d)
    b_r = strassen(strassen(d_r, b), c_r)

    result_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
    result_matrix[:base, :base] = d_r
    result_matrix[base:, base:] = c_r
    result_matrix[:base, base:] = b_r
    return result_matrix

def perm(A, P):
    result = np.zeros((len(A), len(A[0])))
    indexes = []
    for i in range(len(A[0])):
        for j in range(len(A[0])):
            if P[i][j] == 1:
                indexes.append(j)

    for i in range(len(A[0])):
        for j in range(len(A)):
            ind = indexes[i]
            result[j, ind] = A[j, i]
    return result

def lup_decomposition(matrix, m, p):
    if m == 1:
        # 1 L = [1]
        L = np.array([1])
        P = np.eye(p)

        for i in range(p):
            if matrix[0, i] == 1:
                ind = i
                break
            else:
                ind = 0
        P[0, 0], P[ind, ind], P[ind, 0], P[0, ind] = 0, 0, 1, 1

        U = perm(matrix, P)
        return L, U, P

    m_split = m // 2
    # 5) разбить А на В и С
    B = matrix[:m_split, :p]
    C = matrix[m_split:, :p]

    # 6) вызвать МНОЖИТЕЛЬ
    L1, U1, P1 = lup_decomposition(B, m_split, p)

    # 7) вычислить D = CP-1
    D = perm(C, P1.T)

    # 8) E и F первые m/2 матрицы столбцов матрицы U1 и D
    E = U1[:, :m_split]
    F = D[:, :m_split]

    # 9) вычыслить G = D - FE-1U1
    FE_r = strassen(F, reverse(E))

    G = (D - np.matmul(FE_r, U1)) % z

    # 10) пусть G` самые правые p-m/2 стобцов
    G_ = G[:, -(p - m_split):]

    # 11) Вызвать МНОЖИТЕЛЬ и получить L2, U2, P2
    L2, U2, P2 = lup_decomposition(G_, m_split, p-m_split)

    # 12) пусть P3 матрица pxp, левый верхний угол Im/2, правый нижний P2
    I_m_2 = np.eye(m_split)
    P3 = np.vstack((np.hstack((I_m_2, np.zeros((m_split, p-m_split)))), np.hstack((np.zeros((p - m_split, m_split)), P2))))

    # 13) вычислить H = U1P3-1
    H = perm(U1, P3.T)

    # 14) пусть L это матрица mxm из L1, Om/2, FE-1, L2
    O_m_2 = np.zeros((m_split, m_split))
    try:
        L = (np.vstack((np.hstack((L1, O_m_2)), np.hstack((FE_r, L2))))) % z
    except:
        L = (np.vstack((np.hstack((L1[:, np.newaxis], O_m_2)), np.hstack((FE_r, L2[:, np.newaxis]))))) % z

    # 15) пусть U это матрица mxp из H, Om/2 и U2
    U = np.vstack((H, np.hstack((O_m_2, U2))))

    # 16) P = P3 * P1
    P = perm(P3, P1)

    return L, U, P



matrix = []
matrix.append(list(map(int, input().split())))
n = len(matrix[0])
for i in range(n-1):
    matrix.append(list(map(int, input().split())))
matrix = np.array(matrix)

if math.log(n, 2).is_integer() is False:
    matrix = make_matrix(matrix, n)

m = matrix.shape[0]
p = matrix.shape[1]
L, U, P = lup_decomposition(matrix, m, p)

for elem in L[:n, :n].astype('int').tolist():
    print(" ".join(map(str, elem)))
for elem in U[:n, :n].astype('int').tolist():
    print(" ".join(map(str, elem)))
for elem in P[:n, :n].astype('int').tolist():
    print(" ".join(map(str, elem)))