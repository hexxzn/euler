# https://projecteuler.net/problem=4

length = 3  # Length, in digits, of numbers to multiply
lower = int("1" + ("0" * (length - 1)))  # Lower bound of numbers to multiply
upper = int("1" + ("0" * length))  # Upper bound of numbers to multiply
largest_palindrome = 0

for x in range(lower, upper):
    for y in range(lower, upper): 
        product = x * y
        if str(product) == str(product)[::-1]:  # If product is a palindrome
            if product > largest_palindrome:  # If product is larger than previous palindrome
                largest_palindrome = product

print(f'The largest palindrome made from the product of two {length}-digit numbers is {largest_palindrome}.')