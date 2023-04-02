# Anonymous functions - Lambda

def double(val):
    return 2 * val


def square(val):
    return val ** 2


data = [1, 3, 6, 9, 18]

newdata2 = map(square, data)
print(newdata2)

data3 = map(lambda x: x ** 2, data)
print(data3)
