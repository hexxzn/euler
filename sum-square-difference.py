# The sum of the squares of the first ten natural numbers is 385.
# The square of the sum of the first ten natural numbers is 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640. (3025 - 385 = 2640)
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

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
# Time: 0.001       #
# # # # # # # # # # #
