### Problem 34
### https://projecteuler.net/problem=34

from math import factorial
from datetime import datetime
startTime = datetime.now()

sum = 0
for n in range(10, 100000):
    factorial_sum = 0
    num_string = str(n)
    for digit in num_string:
        factorial_sum += factorial(int(digit))
    if factorial_sum == n:
        sum += n
    
print(sum)
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 40730   #
# Time: 0:00.189  #
# # # # # # # # # #
