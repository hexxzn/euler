### Problem 15
### https://projecteuler.net/problem=15

from datetime import datetime
startTime = datetime.now()
from math import factorial

def paths(m, n):
    return int(factorial(m + n) / (factorial(m) * factorial((m + n) - m)))

print(paths(20, 20))
print(datetime.now() - startTime)

# # # # # # # # # # # # #
# Answer: 137846528820  #
# Time: 0:00.001        #
# # # # # # # # # # # # #