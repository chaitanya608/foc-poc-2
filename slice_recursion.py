def slice(my_list, first, last):
    if (len(my_list) == 0):
        return []

    first_el = my_list.pop(0)
    if first > 0:
        rest_sliced = slice(my_list, first - 1, last - 1)
        return rest_sliced
    elif last > 0:
        rest_sliced = slice(my_list, 0, last - 1)
        return [first_el] + rest_sliced
    else:
        return []


print(slice(['a', 'b', 'c', 'd', 'e', 'f'], 2, 4))
