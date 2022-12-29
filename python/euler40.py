### Problem 40
### https://projecteuler.net/problem=40

from datetime import datetime
startTime = datetime.now()

irrational = ""
integer = 0
while len(irrational) <= 1000000:
    irrational += str(integer)
    integer += 1

product = int(irrational[1]) * int(irrational[10]) * int(irrational[100]) * int(irrational[1000]) * int(irrational[10000]) * int(irrational[100000]) * int(irrational[1000000])
print(product)
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 210     #
# Time: 0:00.097  #
# # # # # # # # # #
