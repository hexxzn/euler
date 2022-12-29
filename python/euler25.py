### Problem 25
### https://projecteuler.net/problem=25

from datetime import datetime
startTime = datetime.now()

lstFibonacci = [1, 1]

def fibonacci(digits):
    while len(str(lstFibonacci[-1])) < digits:
        lstFibonacci.append(lstFibonacci[-1] + lstFibonacci[-2])   # generate fibonacci sequence
    return lstFibonacci.index(lstFibonacci[-1]) + 1

print(fibonacci(1000))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 4782    #
# Time: 0:00.026  #
# # # # # # # # # #
