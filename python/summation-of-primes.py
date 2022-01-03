### Problem 10
### https://projecteuler.net/problem=10

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
            if p * i >= limit:
                break
        for i in range(1, limit):
            if p + i in primes:
                p = p + i
                break
            if p * p >= limit:
                return sum(primes)

print(prime_sum(2000000))
print(datetime.now() - startTime)

# # # # # # # # # # # # #
# Answer: 142913828922  #
# Time: 0:01.761        #
# # # # # # # # # # # # #
