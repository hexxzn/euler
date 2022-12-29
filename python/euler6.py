# https://projecteuler.net/problem=6

limit = 100  # Find the sum of squares and square of sum of natural numbers up to this number
sum_of_squares = 0
square_of_sum = 0

for i in range(1, limit + 1):
    sum_of_squares += i ** 2
    square_of_sum += i

square_of_sum = square_of_sum ** 2

print(f'The difference between the sum of the squares and the square of the sum of the first {limit} natural numbers is {square_of_sum - sum_of_squares}.')