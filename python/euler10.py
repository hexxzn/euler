# https://projecteuler.net/problem=10

import math

# Check if number is prime
def is_prime(number):
    limit = math.ceil(math.sqrt(abs(number))) + 1  # Checking beyond square root is redundant

    for i in range(2, limit):
        if number % i == 0:
            return False
    return True

limit = 2000000  # Find the sum of all primes below this number
sum_of_primes = 5  # Start from 5 since 2 and 3 are already included
n = 3  # Check if this number is prime

while n < limit:
    n += 2

    if is_prime(n):
        sum_of_primes += n

print(f'The sum of all prime numbers below {limit} is {sum_of_primes}.')