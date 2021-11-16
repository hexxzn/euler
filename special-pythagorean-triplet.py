from datetime import datetime
startTime = datetime.now()

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
# For example, 3^2 + 4^2 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

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

# # # # # # # # # # # # # #
# Answer: 200, 375, 425   #
# Time: 0.195             #
# # # # # # # # # # # # # #
