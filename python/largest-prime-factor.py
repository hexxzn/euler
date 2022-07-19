# https://projecteuler.net/problem=3

target = 600851475143  # Find the largest prime factor of this number
dividend = target
divisor = 1

while divisor < dividend:
    if dividend % divisor == 0:  # If divisor is a factor of target
        dividend = int(dividend / divisor)  # Result (target) is always prime
    divisor += 1

print(f'The largest prime factor of {target} is {dividend}.')