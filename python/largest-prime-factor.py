### Problem 3
### https://projecteuler.net/problem=3

from datetime import datetime
startTime = datetime.now()

def factor(number):
    dividend = 1

    while dividend < number:
        if number % dividend == 0:
            number = number / dividend
            dividend += 1
        else:
            dividend += 1

    return int(number)

print(factor(600851475143))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 6857    #
# Time: 0:00.002  #
# # # # # # # # # #
