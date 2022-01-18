### Problem 37
### https://projecteuler.net/problem=37

import math
from datetime import datetime
startTime = datetime.now()

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

def is_truncatable_prime_rl(test_number):   # right to left
    num_string = str(test_number)
    for i in range(len(num_string)):
        if not is_prime(int(num_string)):
            return False
        num_string = num_string[1:]
    return True

def is_truncatable_prime_lr(test_number):   # left to right
    num_string = str(test_number)
    for i in range(len(num_string)):
        if not is_prime(int(num_string)):
            return False
        num_string = num_string[:-1]
    return True

truncatable_primes = []
n = 8
while len(truncatable_primes) < 11:
    if is_truncatable_prime_rl(n) and is_truncatable_prime_lr(n):
        truncatable_primes.append(n)
    n += 1

print(sum(truncatable_primes))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 748317  #
# Time: 0:06.602  #
# # # # # # # # # #
