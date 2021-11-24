### Problem 12
### https://projecteuler.net/problem=12

import math

def divisibility(number):
    number = 0
    n = 1
    largest_divisor = 1

    while True:   # generate triangle numbers
        number += n
        n += 1

print(divisibility(144))