### Problem 20
### https://projecteuler.net/problem=20

from datetime import datetime
import math
startTime = datetime.now()

def digitSum(limit):
    list = []
    factorial = math.factorial(limit)   # compute factorial
    strFactorial = str(factorial)   # convert factorial to string
    for i in range(len(strFactorial)):
        list.append(int(strFactorial[i]))   # separate digits and append each to list
    return sum(list)   # return sum of list elements

print(digitSum(100))
print(datetime.now() - startTime)

# # # # # # # # # # 
# Answer: 648     #
# Time: 0:00.001  #
# # # # # # # # # #
