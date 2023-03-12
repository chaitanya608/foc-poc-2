def make_binary(length):
    if length == 0:
        return [""]

    all_but_first = make_binary(length - 1)

    answer = []
    for bits in all_but_first:
        answer.append('0' + bits)
    for bits in all_but_first:
        answer.append('1' + bits)

    return answer


# --> ['000', '001', '010', '011', '100', '101', '110', '111']
print(make_binary(3))
