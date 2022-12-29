### Problem 32
### https://projecteuler.net/problem=32

import re
from datetime import datetime
startTime = datetime.now()

def is_pandigital(number):
    for i in range(1, 9 + 1):
        iterations = [m.start() for m in re.finditer(str(i), number)]
        if len(iterations) != 1:
            return False
    return True

def string_generator():
    products = set()
    for i in range(1, 50):
        for j in range(i, 2000):
            product = i * j
            number_string = str(i) + str(j) + str(product)
            if len(number_string) == 9:
                if is_pandigital(number_string):
                    products.add(product)
    return max(products), sum(products)

print(string_generator())
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 45228   #
# Time: 0:01.639  #
# # # # # # # # # #
