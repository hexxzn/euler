### Problem 10
### https://projecteuler.net/problem=10

import math
from datetime import datetime
startTime = datetime.now()

def prime_sum(limit):
    primes = set()
    for i in range(2, limit):
        primes.add(i)

    p = 2
    while True:
        for i in range(p, limit):
            if p * i in primes:
                primes.remove(p * i)

        for i in range(1, limit):
            if p + i in primes:
                print(math.floor((p / limit ** 0.5) * 100), "%")
                p = p + i
                break
            elif p * p >= limit:
                return sum(primes)

print(prime_sum(2000000))
print(datetime.now() - startTime)

# # # # # # # # # # # # #
# Answer: 142913828922  #
# Time: 1:26.522        #
# # # # # # # # # # # # #
