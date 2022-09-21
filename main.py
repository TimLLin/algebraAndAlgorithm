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
        print(level)
        count = 1
        while count + 2**level <= n:
            dictOfValue[len(dictOfValue)] = 'gate' +str(level)
            count += 1
        print(count)
        level += 1

    print(dict(dictOfValue))
    print(prefix)
    print(input)
prefixSum(2)