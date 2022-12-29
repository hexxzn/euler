### Problem 41
### https://projecteuler.net/problem=41

import math
from datetime import datetime
startTime = datetime.now()

# def is_prime_old(test_number):
#     limit = math.ceil(math.sqrt(abs(test_number))) + 1
#     for i in range(2, limit):
#         if test_number % i == 0:
#             return False
#     return True

def is_prime(test_number):
    if test_number == 1 or test_number == 4 or test_number == 6:
        return False
    if test_number == 2 or test_number == 3 or test_number == 5:
        return True
    limit = math.ceil(math.sqrt(abs(test_number))) + 1
    for i in range(7, limit, 2):
        sum = 0
        for char in str(test_number):
            sum += int(char)
            if sum == 3 or sum == 6 or sum == 9:
                return False
        if test_number % i == 0:
            return False
    return True

def is_pandigital(number):
    number_string = str(number)
    for i in range(1, len(number_string) + 1):
        if str(i) not in number_string:
            return False
    return True

def pandigital_prime():
    for i in range(987654321, 0, -1):
        if is_prime(i):
            if is_pandigital(i):
                return i

print(is_prime(47))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 7652413
# Time:
# # # # # # # # # #
