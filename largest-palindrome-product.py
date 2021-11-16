from datetime import datetime
startTime = datetime.now()

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

largest_palindrome = 0

for multiplicand in range(1, 1000):             
    for multiplier in range(1, 1000):           
        result = multiplier * multiplicand      
        if str(result) == str(result)[::-1]:    # Check if result is palindrome by converting to string and comparing to reverse of itself
            int(result)
            if result > largest_palindrome:     # Check if confirmed palindrome is largest palindrome
                largest_palindrome = result

print(largest_palindrome)
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 906609  #
# Time: 0.552     #
# # # # # # # # # #
