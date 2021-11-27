### Problem 12
### https://projecteuler.net/problem=12

from datetime import datetime
startTime = datetime.now()

def divisors(n):
    count = 1
    triangle = 0
    while True:
        divisors = 0
        triangle += count
        count += 1
        for i in range(1, triangle):
            if i > triangle / 2:
                break
            if triangle % i == 0:
                divisors += 1
                if divisors > n:
                    return triangle

print(divisors(100))
print(datetime.now() - startTime)

# # # # # #
# Answer: #
# Time:   #
# # # # # #