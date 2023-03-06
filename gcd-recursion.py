"""
Write a function gcd(num1, num2) that takes two non-negative integers and computes the greatest common divisor of num1 and num2.
To simplify the problem, you may assume that the greatest common divisor of zero and any non-negative integer is the integer itself.
For an extra challenge, your programs should only use subtraction. Hint: If you get stuck, try searching for "Euclid's Algorithm".
"""


def gcd(num1, num2):
    if num2 > num1:
        return gcd(num2, num1)

    remainder = num1 % num2

    if remainder == 0:
        return num2
    else:
        return gcd(num2, remainder)


result = gcd(96, 128)
print("gcd: " + str(result))
