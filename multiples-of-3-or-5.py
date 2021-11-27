### Problem 1
### https://projecteuler.net/problem=1

from datetime import datetime
startTime = datetime.now()

sum = 0

for i in range(1000):
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i

print(sum)
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 233168  #
# Time: 0:00.001  #
# # # # # # # # # #
