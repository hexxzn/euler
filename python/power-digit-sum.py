### Problem 161
### https://projecteuler.net/problem=16

from datetime import datetime
startTime = datetime.now()

def digit_sum(exp):
    number = 2 ** exp
    digits = [int(a) for a in str(number)]
    answer = sum(digits)
    return answer

print(digit_sum(1000))
print(datetime.now() - startTime)

# # # # # # # # # # 
# Answer: 1366    #
# Time: 0:00.001  #
# # # # # # # # # #
