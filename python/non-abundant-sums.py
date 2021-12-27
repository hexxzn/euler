### Problem 23
### https://projecteuler.net/problem=23

from datetime import datetime
import math
startTime = datetime.now()

def nonAbundant(limit):
    setIntegers = {n for n in range(1, limit)}   # generate set of all integers in range(1, limit)
    setAbundant = {12}
    
    for n in range(13, limit):   # generate set of abundant numbers
        setDivisors = {1}
        for i in range(math.ceil(n ** 0.5), 1, -1):
            if n % i == 0:
                setDivisors.add(i)
                setDivisors.add(int(n / i))
        if sum(setDivisors) > n:
            setAbundant.add(n)

    for i in setAbundant:   # remove abundant sums from set integers
        for j in setAbundant:
            if i < j or i + j >= limit:
                break
            if i + j in setIntegers:
                setIntegers.remove(i + j)

    return sum(setIntegers)

print(nonAbundant(28124))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 4179871 #
# Time: 0:03.341  #
# # # # # # # # # #
