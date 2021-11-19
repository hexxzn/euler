# Prime factors are factors of a number that are, themselves, prime numbers.
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

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

# # # # # # # # #
# Answer: 6857  #
# Time: 0.002   #
# # # # # # # # #
