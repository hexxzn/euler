### Problem 10
### https://projecteuler.net/problem=10

from datetime import datetime
startTime = datetime.now()

def prime_sum(limit):
    primes = set()
    for i in range(2, limit):   # generate set of whole numbers up to limit. non-primes will be removed.
        primes.add(i)

    p = 2
    while True:   # Sieve of Eratosthenes: Remove non-primes from set
        for i in range(p, limit):   # start sweep from p squared since smaller multiples have already been removed (or don't exist to begin with)
            if p * i in primes:
                primes.remove(p * i)   # remove multiples of p
            if p * i >= limit:
                break   # stop removing multiples when result is greater than limit

        for i in range(1, limit):
            if p + i in primes:
                p = p + i   # set p equal to the next largest number in set since multiples of anything below have already been removed
                break
            if p * p >= limit:   # sieve is complete since each sweep begins at p squared
                return sum(primes)

print(prime_sum(2000000))
print(datetime.now() - startTime)

# # # # # # # # # # # # #
# Answer: 142913828922  #
# Time: 0:01.761        #
# # # # # # # # # # # # #
