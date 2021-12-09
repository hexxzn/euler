### Problem 11
### https://projecteuler.net/problem=1

from datetime import datetime
startTime = datetime.now()

def multiplesum(limit):
    sum = 0

    for i in range(limit):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i

    return sum

print(multiplesum(1000))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 233168  #
# Time: 0:00.001  #
# # # # # # # # # #
