# https://projecteuler.net/problem=9

import math

def pythagorean_triplet(target):
    for a in range(500):
        for b in range(a, 500):
            c = math.hypot(a, b)
            sum = a + b + c
            if sum == target:
                return a * b * c

target = 1000  # Find pythagorean triplet for which a + b + c = this number
product = pythagorean_triplet(target)
print(f'The product a * b * c for which a + b + c = {target} is {int(product)}.')