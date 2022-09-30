from collections import defaultdict
def compressor(n):
    def not_gate(gate_out, gate_in):
        return f"GATE {gate_out} NOT {gate_in}"
    def and_gate(gate_out, gate_in1, gate_in2):
        return f"GATE {gate_out} AND {gate_in1} {gate_in2}"
    def or_gate(gate_out, gate_in1, gate_in2):
        return f"GATE {gate_out} OR {gate_in1} {gate_in2}"

    dictOfValue = defaultdict(dict)
    for i in range(3*n):
        dictOfValue[i] = i
    output = [0] * (2*(n+1))


    for i in range(n):
        dictOfValue[len(dictOfValue)] = not_gate(len(dictOfValue), i)
        dictOfValue[len(dictOfValue)] = and_gate(len(dictOfValue), n+i, 2*n+i)
        dictOfValue[len(dictOfValue)] = not_gate(len(dictOfValue), len(dictOfValue)-1)
        dictOfValue[len(dictOfValue)] = or_gate(len(dictOfValue), n+i, 2*n+i)
        dictOfValue[len(dictOfValue)] = and_gate(len(dictOfValue), len(dictOfValue)-2, len(dictOfValue)-1)
        dictOfValue[len(dictOfValue)] = and_gate(len(dictOfValue), len(dictOfValue)-5, len(dictOfValue)-1)
        dictOfValue[len(dictOfValue)] = not_gate(len(dictOfValue), len(dictOfValue)-3)
        dictOfValue[len(dictOfValue)] = or_gate(len(dictOfValue), len(dictOfValue)-6, len(dictOfValue)-1)
        dictOfValue[len(dictOfValue)] = and_gate(len(dictOfValue), i, len(dictOfValue)-1)
        dictOfValue[len(dictOfValue)] = or_gate(len(dictOfValue), len(dictOfValue) - 4, len(dictOfValue) - 1)
        output[i] = (len(dictOfValue)-1)
        dictOfValue[len(dictOfValue)] = and_gate(len(dictOfValue), i, len(dictOfValue)-6)
        dictOfValue[len(dictOfValue)] = or_gate(len(dictOfValue), len(dictOfValue)-10, len(dictOfValue) - 1)
        output[i+n+2] = (len(dictOfValue)-1)

    dictOfValue[len(dictOfValue)] = and_gate(len(dictOfValue), 0, 3*n)
    output[n] = len(dictOfValue)-1
    output[n+1] = len(dictOfValue)-1

    for elem in list(dictOfValue.values())[3*n:]:
        print(elem)

    for i in range(len(output)):
        print(f"OUTPUT {i} {output[i]}")
n = int(input())
compressor(n)