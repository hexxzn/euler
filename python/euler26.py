### Problem 26
### https://projecteuler.net/problem=26

from datetime import datetime
from decimal import *
getcontext().prec = 10000
startTime = datetime.now()

def cycle(limit):
    cycleLength = 0   # represents the length of the longest cycle found

    for d in range(1, limit):
        strTest = str(Decimal(1) / Decimal(d))[len(str(d)) + 1:-1]   # generates decimal string and removes last digit (rounded digit)
        strTest = strTest[::-1]   # reverses string to avoid leading zeroes

        for i in range(1, (len(strTest) // 2)):   # checks for repeated segments in decimal string
            strFirst = strTest[0:i]
            strSecond = strTest[i:len(strFirst) + i]
            if strFirst == strSecond:   # if repeated segment found
                if len(strFirst) > cycleLength:   # if repeated segment longer than all previous segments
                    cycleLength = len(strFirst)
                    answer = d
                break
    
    return answer

print(cycle(1000))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 983     #
# Time: 0:00.179  #
# # # # # # # # # #
