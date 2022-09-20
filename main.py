import math
def prefixSum(n):
    input = [x for x in range(n)]
    prefix = [0] * n
    dict = {0: 0}
    for i in input:
        dict[i] = i
    for i in input[1:]:
        if i < len(input):
            prefix[i] = prefix[i-1] + input[i]
            dict[i + len(input)-1] = [prefix[i], (i-1, i)]

    print(dict)
    print(prefix)
    print(input)
prefixSum(3)