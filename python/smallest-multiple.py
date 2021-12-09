### Problem 5
### https://projecteuler.net/problem=5

from datetime import datetime
startTime = datetime.now()

def divisibility(limit):   # return the first number evenly divisible by all numbers from 1 to limit
    number = 2520
    increment = 2520
    while True:
        for i in range(1, limit + 1):
            if number % i != 0:
                break
            if i == limit:
                return number
        number += increment

print(divisibility(20))
print(datetime.now() - startTime)

# # # # # # # # # # #
# Answer: 232792560 #
# Time: 0:00.049    #
# # # # # # # # # # #
