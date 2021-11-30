### Problem 4
### https://projecteuler.net/problem=4

from datetime import datetime
startTime = datetime.now()

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
# Time: 0:00.552  #
# # # # # # # # # #
