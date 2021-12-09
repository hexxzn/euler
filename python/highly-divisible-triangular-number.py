### Problem 121
### https://projecteuler.net/problem=12

from datetime import datetime
import math
startTime = datetime.now()

def divisors(n):   # finds first triangle number with over n divisors
    count = 1
    triangle = 0
    while True:   # generates triangle numbers
        divisors = 0
        triangle += count
        count += 1
        for i in range(math.ceil(triangle ** 0.5), 0, -1):   # tests divisors counting down from square root of triangle number
            if triangle % i == 0:
                divisors += 2   # add two to divisor count for each division that produces no remainder
        if (triangle ** 0.5).is_integer() == True:   # if triangle number square root is a perfect square, subtract one from divisor count since square root was initially counted as two divisors
            divisors -= 1
        if divisors > n:
            return triangle, divisors

print(divisors(500))
print(datetime.now() - startTime)

# # # # # # # # # # #
# Answer: 76576500  #
# Time: 0:04.914    #
# # # # # # # # # # #
