### Problem 27
### https://projecteuler.net/problem=27

import math
from datetime import datetime
startTime = datetime.now()

def is_prime(test_number):
    limit = math.ceil(math.sqrt(abs(test_number)))
    for i in range(2, limit):
        if test_number % i == 0:
            return False
    return True

def max_primes(limit):
    max_n = 0
    max_a = 0
    max_b = 0
    for a in range(-limit + 1, limit + 1): 
        for b in range(-limit, limit + 2): 
            n = 0
            result = (n ** 2) + (a * n) + b
            while is_prime(result) == True:
                result = (n ** 2) + (a * n) + b
                if not is_prime(result):
                    break
                if n > max_n:
                    max_n = n
                    max_a = a
                    max_b = b
                n += 1
    return max_a * max_b

print(max_primes(1000))
print(datetime.now() - startTime)

# # # # # # # # # # 
# Answer: -59231  #
# Time: 0:13.745  #
# # # # # # # # # #
