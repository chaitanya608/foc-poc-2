def bin_to_dec(bin_num):
    """
    Recursion:
    converts a binary string to its decimal value.
    """
    if len(bin_num) == 0:
        return 0

    first = bin_num[0]
    pos = len(bin_num) - 1

    dec_value = (2 ** pos) * int(first)

    return dec_value + bin_to_dec(bin_num[1:])


print(bin_to_dec('100100100110'))  # --> 2342
