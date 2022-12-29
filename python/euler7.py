# https://projecteuler.net/problem=7

import math

# Check if number is prime
def is_prime(number):
    limit = math.ceil(math.sqrt(abs(number))) + 1  # Checking beyond square root is redundant

    for i in range(2, limit):
        if number % i == 0:
            return False
    return True

n = 10001  # Find the nth prime
prime = 3  # Check if this number is prime
count = 2  # The n value of current prime

while count < n:  # Stop on nth prime
    prime += 2

    if is_prime(prime):
        count += 1

print(f'The nth({n}) prime number is {prime}.')
