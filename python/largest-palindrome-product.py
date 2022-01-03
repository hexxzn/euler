### Problem 4
### https://projecteuler.net/problem=4

from datetime import datetime
startTime = datetime.now()

def largest_palindrome(length):
    palindrome = 0
    for x in range(1, int("9" * length) + 1):             
        for y in range(1, int("9" * length) + 1):           
            result = x * y      
            if str(result) == str(result)[::-1] and result > palindrome:
                palindrome = result
    return palindrome

print(largest_palindrome(3))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 906609  #
# Time: 0:00.326  #
# # # # # # # # # #
