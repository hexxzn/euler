# https://projecteuler.net/problem=5

limit = 20  # Test if dividend is evenly divisible by all numbers from 1 up to this number
dividend = 1  # First number to test for divisibility
increment = [1, 1]
answer = 0

while answer == 0:
    for i in range(1, limit + 1):
        if dividend % i != 0:  # If dividend is not evenly divisible by i
            break

        if i == limit:  # If dividend is divisible by all numbers in range
            answer = dividend

        if i > increment[1]:  # If current dividend is more divisible than previous
            increment[0] = dividend  # Dividend becomes the new increment
            increment[1] = i  # i is the highest number dividend is evenly divided by

    dividend += increment[0]

print(f'The smallest positive number that is evenly divisible by all numbers from 1 to {limit} is {answer}.')