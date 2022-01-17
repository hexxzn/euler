### Problem 36
### https://projecteuler.net/problem=36

from datetime import datetime
startTime = datetime.now()

def is_palindrome(test_number):
    if str(test_number) == str(test_number)[::-1]:
        return True
    return False

palindrome_sum = 0
for n in range(1000000):
    n_binary = format(n, "b")
    if is_palindrome(n) and is_palindrome(n_binary):
        palindrome_sum += n

print(palindrome_sum)
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 872187  #
# Time: 0:01.424  #
# # # # # # # # # #
