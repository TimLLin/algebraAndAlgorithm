import numpy as np

base = 10000
def make_matrix(graph, n):
    matrix = np.zeros((n, n), dtype='float64')
    for edge in graph:
        matrix[edge[0], edge[1]] = np.random.randint(1, base)
    return matrix

def determinant(matrix):
    n = matrix.shape[0]
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if matrix[j, i] != 0.0:
                curr = (matrix[j, i] / matrix[i, i]) % base
                matrix[j, i+1:n] = (matrix[j, i+1:n] - curr * matrix[i, i+1:n]) % base

    diag = np.diag(matrix)
    return np.prod(diag) % base

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

det = determinant(matrix)

if det != 0:
    print('yes')
elif det == 0:
    print('no')