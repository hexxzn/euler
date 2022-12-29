# https://projecteuler.net/problem=1

limit = 1000  # Find the sum of all multiples of 3 or 5 below this number
sum = 0

for i in range(limit):
    if i % 3 == 0 or i % 5 == 0:  # if i is divisible by 3 or 5
        sum += i  # Add i to sum

print(f'The sum of all multiples of 3 or 5 below {limit} is {sum}.')