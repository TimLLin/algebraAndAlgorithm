import numpy as np
from itertools import product

def multipol(n):
    np_truth_table = np.zeros((2**(2**n), 2**n), 'bool')
    truth_table_check = set()

    gates = []
    outputs = []

    lst1 = [[0, 1]] * n
    variables = np.array(list(product(*lst1)), 'bool').T

    np_truth_table[:n] = variables
    for i in variables:
        truth_table_check.add(tuple(i))


    #not bloke
    for i in range(n):
        elem = np.invert(np_truth_table[i])
        if tuple(elem) not in truth_table_check:
            truth_table_check.add(tuple(elem))
            np_truth_table[len(truth_table_check)-1] = elem

            gates.append(f'GATE {(len(truth_table_check)-1)} NOT {i}')
            outputs.append(f'OUTPUT {len(outputs)+n} {(len(truth_table_check)-1)}')


    #and block
    for i in range(len(truth_table_check)):
        for j in range(1, len(truth_table_check)):
            elem = np_truth_table[i] & np_truth_table[j]
            if tuple(elem) not in truth_table_check:
                truth_table_check.add(tuple(elem))
                np_truth_table[len(truth_table_check) - 1] = elem

                gates.append(f'GATE {(len(truth_table_check) - 1)} AND {i} {j}')
                outputs.append(f'OUTPUT {len(outputs) + n} {(len(truth_table_check) - 1)}')

    #or block
    for i in range(len(truth_table_check)):
        for j in range(1, len(truth_table_check)):
            elem =  np_truth_table[i] | np_truth_table[j]
            if tuple(elem) not in truth_table_check:
                truth_table_check.add(tuple(elem))
                np_truth_table[len(truth_table_check) - 1] = elem

                gates.append(f'GATE {(len(truth_table_check) - 1)} OR {i} {j}')
                outputs.append(f'OUTPUT {len(outputs) + n} {(len(truth_table_check) - 1)}')


    for i in range(n):
        outputs.insert(i, f'OUTPUT {i} {i}')
    for elem in gates:
        print(elem)
    for elem in outputs:
        print(elem)

multipol(4)

