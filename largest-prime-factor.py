### Problem 3
### https://projecteuler.net/problem=3

from datetime import datetime
startTime = datetime.now()

number = 600851475143
dividend = 1

while(dividend < number):               # This loop is essentially building a factor tree
    if number % dividend == 0:          # Number and dividend become branches of the factor tree
        number = number / dividend
        dividend += 1
    else:
        dividend += 1

print(int(number))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 6857    #
# Time: 0:00.002  #
# # # # # # # # # #
