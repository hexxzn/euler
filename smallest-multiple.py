from datetime import datetime
startTime = datetime.now()

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divisor_max = 20        # find number divisible by all numbers from 1 to this variable
increment = 2520        
dividend = 2520         # set to same as increment

def divisible(test_number):
    for i in range(1, divisor_max+1):
        if test_number % i != 0:
            return False
    return True

while not divisible(dividend):
    dividend += increment
    divisible(dividend)

print(dividend)
print(datetime.now() - startTime)

# # # # # # # # # # # #
# Answer: 232792560   #
# Time: 0.293         #
# # # # # # # # # # # #
