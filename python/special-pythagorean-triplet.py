### Problem 91
### https://projecteuler.net/problem=9

from datetime import datetime
startTime = datetime.now()

a = 1
b = 1
c = 1

for i in range(1, 500):
    a += 1
    b = 1
    for i in range(1, 500):
        b += 1
        c = a ** 2 + b ** 2
        if (a + b) + (c ** 0.5) == 1000:
            print(a, b, c)
            print("product =", a * b * (c ** 0.5))

print(datetime.now() - startTime)

# # # # # # # # # # # # #
# Answer: 200, 375, 425 #
# Time: 0:00.195        #
# # # # # # # # # # # # #
