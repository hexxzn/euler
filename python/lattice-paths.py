### Problem 15
### https://projecteuler.net/problem=15

from datetime import datetime
from math import factorial
startTime = datetime.now()

def paths(rows, columns):
    return int(factorial(rows + columns) / (factorial(rows) * factorial((rows + columns) - rows)))

print(paths(20, 20))
print(datetime.now() - startTime)

# # # # # # # # # # # # #
# Answer: 137846528820  #
# Time: 0:00.001        #
# # # # # # # # # # # # #
