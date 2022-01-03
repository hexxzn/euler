### Problem 8
### https://projecteuler.net/problem=8

from datetime import datetime
startTime = datetime.now()

def largest_series_product(thousand_digit_number):
    thousand_digits = []
    thirteen_digits = []
    largest_product = 0

    for char in thousand_digit_number:
        if char != "\n":
            thousand_digits.append(char)
    for i in range(0, 988):
        thirteen_digits = thousand_digits[i:i+13]
        product = 1
        for digit in thirteen_digits:
            product *= int(digit)
            if product > largest_product:
                largest_product = product
    
    return largest_product

print(largest_series_product(open("data\p8-number").read()))
print(datetime.now() - startTime)

# # # # # # # # # # # #
# Answer: 23514624000 #
# Time: 0:00.005      #
# # # # # # # # # # # #
