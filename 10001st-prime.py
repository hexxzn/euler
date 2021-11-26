### Problem 7
### https://projecteuler.net/problem=7

from datetime import datetime
startTime = datetime.now()

def nth_prime(n):
    primes = [2]
    test = 3
    while True:
        for i in range(2, test):
            if test % i == 0 :
                break
            if i >= test ** 0.5:
                primes.append(test)
                break

        if len(primes) == n:
            return primes[n-1]

        test += 2

print(nth_prime(10001))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 104743  #
# Time: 0.753     #
# # # # # # # # # #
