import math
from collections import defaultdict
def prefixSum(n):
    input = [x for x in range(n)]
    prefix = [0] * n
    dictOfValue = defaultdict(dict)
    for i in input:
        dictOfValue[i] = i
    level = 1
    index = 1
    while level <= math.log2(n):
        count = 0
        while count + 2**level <= n:
            dictOfValue[len(dictOfValue)] = 'gate' +str(level)
            count +=1

        level += 1

    print(level)
    print(dict(dictOfValue))
    print(prefix)
    print(input)
prefixSum(4)