from datetime import datetime
startTime = datetime.now()

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

test_number = 3
prime = 1
prime_number_to_find = 10001

def is_prime(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

print("( 1 ) 2")
while prime < prime_number_to_find:
    if is_prime(test_number):
        prime += 1
        
    test_number += 2

print("(",prime,")",test_number)
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 104745  #
# Time: 43.411    #
# # # # # # # # # #
