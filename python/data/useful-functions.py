import math
import re

def is_prime(test_number):
    if test_number == 1:
        return False
    if test_number == 2:
        return True
    limit = math.ceil(math.sqrt(abs(test_number))) + 1
    for i in range(2, limit):
        if test_number % i == 0:
            return False
    return True

def is_palindrome(test_number):
    if str(test_number) == str(test_number)[::-1]:
        return True
    return False

def is_pandigital(number):
    for i in range(1, 9 + 1):
        iterations = [m.start() for m in re.finditer(str(i), number)]
        if len(iterations) != 1:
            return False
    return True