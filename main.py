from collections import defaultdict
def compressor(n):
    def not_gate(gate_out, gate_in):
        return f"GATE {gate_out} NOT {gate_in}"
    def and_or_gate(gate_out, oper, gate_in1, gate_in2):
        return f"GATE {gate_out} {oper} {gate_in1} {gate_in2}"

    dictOfValue = defaultdict(dict)
    for i in range(3*n):
        dictOfValue[i] = i
    output = []


    for i in range(n):
        dictOfValue[len(dictOfValue)] = not_gate(len(dictOfValue), )
            f"GATE {len(dictOfValue)} NOT {i}"
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} AND {n+i, 2*n+i}"
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} NOT {len(dictOfValue)-1}"
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} OR {n+i, 2*n+i}"
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} AND {len(dictOfValue)-2, len(dictOfValue)-1}"
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} AND {len(dictOfValue)-5, len(dictOfValue)-1}"
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} NOT {len(dictOfValue)-3}"
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} OR {len(dictOfValue)-6, len(dictOfValue)-1}"
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} AND {i, len(dictOfValue)-1}"
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} OR {len(dictOfValue) - 4, len(dictOfValue) - 1}"
        output.append(len(dictOfValue))
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} AND {i, len(dictOfValue)-6}"
        dictOfValue[len(dictOfValue)] = f"GATE {len(dictOfValue)} OR {len(dictOfValue)-10, len(dictOfValue) - 1}"



    for elem in list(dictOfValue.values())[3*n:]:
        print(elem)

compressor(2)