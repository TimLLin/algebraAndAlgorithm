import numpy as np

base = 100000000
def make_matrix(graph, n):
    matrix = np.zeros((n, n), dtype='float64')
    for edge in graph:
        matrix[edge[0], edge[1]] = np.random.randint(1, base)
    return matrix

def det(matrix):
    n = matrix.shape[0]
    matrix = matrix.tolist()
    n = len(matrix)
    d, sign = 1, 1
    for i in range(n):
        if matrix[i][i] == 0:
            j = next((j for j in range(i + 1, n) if matrix[j][i] != 0), None)
            if j is None:
                return 0
            matrix[i], matrix[j] = matrix[j], matrix[i]
            sign = -sign
        d *= matrix[i][i]
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i + 1, n):
                matrix[j][k] -= factor * matrix[i][k]
    return d * sign

n = int(input())
graph = []
size = 0
for _ in range(n):
    edge = list(map(int, input().split()))
    graph.append(edge)
    curr_max = max(edge)
    if curr_max > size:
        size = curr_max

matrix = make_matrix(graph, size+1)
print(type(np.linalg.det(matrix)))
cur_det = det(matrix)
print(type(cur_det))

