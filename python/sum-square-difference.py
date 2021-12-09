### Problem 61
### https://projecteuler.net/problem=6

from datetime import datetime
startTime = datetime.now()

limit = 100

def sum_of_squares(limit):
    limit += 1
    sum = 0
    for i in range(1, limit):
        sum += (i ** 2)
    return sum

def square_of_sums(limit):
    limit += 1
    sum = 0
    for i in range(1, limit):
        sum += i
    square = (sum ** 2)
    return square

print(square_of_sums(limit)-sum_of_squares(limit))
print(datetime.now() - startTime)

# # # # # # # # # # #
# Answer: 25164150  #
# Time: 0:00.001    #
# # # # # # # # # # #
