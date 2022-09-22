import math
from collections import defaultdict
def prefixSum(n):
    input = [x for x in range(n)]

    dictOfValue = defaultdict(dict)
    for i in input:
        dictOfValue[i] = i

    prefix = list(dictOfValue.keys())
    level = 0

    while level <= math.log2(n):
        count = 0
        #print(prefix)
        while count + 2**level+1 <= n:
            #if count+1 <= 2**level:
            #    prefix[count] = prefix[count]
            #    print(prefix)
            #elif count+1>2**level:
            #    prefix[count] = list(dictOfValue.keys())[len(dictOfValue)-1]
            #print(prefix[count])
            dictOfValue[len(dictOfValue)] = [prefix[count], prefix[count+2**level]]

            #print(len(dictOfValue), level)
            count += 1
        prefix = prefix[:2**level] + list(dictOfValue.keys())[len(dictOfValue)+2**level- n: len(dictOfValue)]
        #print(prefix[:2** level])
        #print(list(dictOfValue.keys())[len(dictOfValue)+2**level- n: len(dictOfValue)])
        #prefix = prefix[:2** level] + list(dictOfValue.keys())[len(dictOfValue)-1:2 ** level]
        level += 1
    for key, elem in dictOfValue.items():
        if key >= n:
            print(f"GATE {key} OR {elem[0]} {elem[1]}")


    print(f"OUTPUT {0} {0}")
    for i in range(1, n):
        print(f"OUTPUT {i} {prefix[i]}")


    #print(dict(dictOfValue))
    #print(prefix)
n = int(input())
prefixSum(n)