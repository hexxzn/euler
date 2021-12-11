### Problem 6
### https://projecteuler.net/problem=6

from datetime import datetime
startTime = datetime.now()

def difference(limit):
    limit += 1
    
    sum = 0
    for i in range(1, limit):
        sum += (i ** 2)
    sum_squares = sum

    sum = 0
    for i in range(1, limit):
        sum += i
    square_sums = (sum ** 2)

    return square_sums - sum_squares

print(difference(100))
print(datetime.now() - startTime)

# # # # # # # # # # #
# Answer: 25164150  #
# Time: 0:00.001    #
# # # # # # # # # # #
