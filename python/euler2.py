# https://projecteuler.net/problem=2

limit = 4000000  # Do not consider Fibonacci sequence terms greater than this number
a, b, c = 0, 1, 2  # First three terms in Fibonacci sequence
sum = 0

while b <= limit:
    a = b  # a becomes b
    b = c  # b becomes c
    c = a + b  # c becomes the sum of a and b

    if a % 2 == 0:  # If a is even
        sum += a  # Add to sum

print(f'The sum of the even-valued terms whose values do not exceed {limit}, is {sum}.')