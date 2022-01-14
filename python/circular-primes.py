### Problem 35
### https://projecteuler.net/problem=35

import math
from datetime import datetime
startTime = datetime.now()

def is_prime(test_number):
    limit = math.ceil(math.sqrt(abs(test_number))) + 1
    for i in range(2, limit):
        if test_number % i == 0 and test_number != 2:
            return False
    return True

def circulate(num):
    circulation = []
    num_string = str(num)
    rotations = len(num_string) - 1
    circulation.append(num)
    for i in range(rotations):
        num_string = num_string[-1] + num_string[0:-1]
        circulation.append(int(num_string))
    return circulation

circular_primes = set()
for n in range(2, 1000000):
    test_numbers = circulate(n)
    for test_number in test_numbers:
        if not is_prime(test_number):
            break
        if test_number == test_numbers[-1]:
            circular_primes.add(n)
            
print(len(circular_primes))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 55      #
# Time: 0:12.374  #
# # # # # # # # # #
