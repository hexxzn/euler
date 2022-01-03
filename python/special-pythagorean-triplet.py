### Problem 9
### https://projecteuler.net/problem=9

from datetime import datetime
startTime = datetime.now()

def pythagorean_triplet():
    c = 1
    for a in range(500):
        for b in range(a, 500):
            c = a ** 2 + b ** 2
            if (a + b) + (c ** 0.5) == 1000:
                return int(a * b * (c ** 0.5))

print(pythagorean_triplet())
print(datetime.now() - startTime)

# # # # # # # # # # #
# Answer: 31875000  #
# Time: 0:00.055    #
# # # # # # # # # # #
