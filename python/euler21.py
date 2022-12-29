### Problem 21
### https://projecteuler.net/problem=21

from datetime import datetime
import math
startTime = datetime.now()

divisorSum = [0]
amicable = []

def amicableSum(limit):
    for n in range(1, limit):
        divisors = []
        for i in range(math.floor(n/2), 0, -1):
            if n % i == 0:
                divisors.append(i)
        divisorSum.append(sum(divisors))

    for i in range(1, len(divisorSum)):
        if i not in amicable and i in divisorSum and divisorSum[i] == divisorSum.index(i) and i != divisorSum[i]:
            amicable.append(i)
            amicable.append(divisorSum[i])

    return sum(amicable)

print(amicableSum(10000))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 31626   #
# Time: 0:02.846  #
# # # # # # # # # #
