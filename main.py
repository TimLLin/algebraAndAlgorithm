import math
from collections import defaultdict
def prefixSum(n):
    input = [x for x in range(n)]
    prefix = [0] * n
    dictOfValue = defaultdict(dict)
    for i in input:
        dictOfValue[i] = i
    level = 0
    index = 1
    while level <= math.log2(n):
        count = 0
        while count + 2**level+1 <= n:
            dictOfValue[len(dictOfValue)] = [count, count+2**level*n-(n-1)]
            print(len(dictOfValue), level)
            count += 1
        level += 1
    for key, elem in dictOfValue.items():
        if key >= n:
            print(f"GATE {key} OR {elem[0]} {elem[1]}")

    out_count = 0

    for i in range(n):
        print(f"OUTPUT {i} {i+out_count}")
        out_count+=1

    print(dict(dictOfValue))
prefixSum(4)