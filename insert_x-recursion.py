def insert_x(my_string):
    """
    * sample input: "catdog"
    * expected output: "cxaxtxdxoxg"
    """
    if len(my_string) == 0:
        return ""
    else:
        first = my_string[0]
        rest_inserted = insert_x(my_string[1:])

        if rest_inserted == "":
            return first
        else:
            return first + "x" + rest_inserted


result = insert_x("Chaitanya")
print("result: " + result)
