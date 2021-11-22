### Problem 7
### https://projecteuler.net/problem=7

from datetime import datetime
startTime = datetime.now()

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
