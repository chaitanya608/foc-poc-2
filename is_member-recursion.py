def is_member(my_list, elem):
    if len(my_list) == 0:
        return False

    first = my_list[0]
    rest = my_list[1:]

    if first == elem:
        return True

    return is_member(rest, elem)


def test_is_member():
    """
    Some test cases for is_member
    """
    print("Computed:", is_member([], 1), "Expected: False")
    print("Computed:", is_member([1], 1), "Expected: True")
    print("Computed:", is_member(['c', 'a', 't'], 't'), "Expected: True")
    print("Computed:", is_member(['c', 'a', 't'], 'd'), "Expected: False")


test_is_member()
