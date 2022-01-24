### Problem 39
### https://projecteuler.net/problem=39

import math
from datetime import datetime
startTime = datetime.now()

p_solutions = {}

for a in range(1, 1000 + 1):
    for b in range(1, 1000 + 1):
        c_squared = (a ** 2) + (b ** 2)
        c = math.sqrt(c_squared)
        if c % 1 == 0:
            c = int(c)
            p = int(a + b + c)
            if p <= 1000:
                if p in p_solutions:
                    p_solutions[p] += 1
                else: p_solutions[p] = 1

print(max(p_solutions, key = p_solutions.get))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 840     #
# Time: 0:00.707  #
# # # # # # # # # #
