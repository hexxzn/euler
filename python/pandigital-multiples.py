### Problem 38
### https://projecteuler.net/problem=38

import re
from datetime import datetime
startTime = datetime.now()

def is_pandigital(number):
    for i in range(1, 9 + 1):
        iterations = [m.start() for m in re.finditer(str(i), number)]
        if len(iterations) != 1:
            return False
    return True

largest_product = 0
for n in range(1, 9999 + 1):
    test_number = ""
    for i in range(1, 987654321 + 1):
        product = n * i
        test_number += str(product)
        if len(test_number) > 9:
            break
        if len(test_number) == 9 and i > 1:
            if is_pandigital(test_number) and int(test_number) > largest_product:
                print(test_number)
                largest_product = int(test_number)

print(largest_product)
print(datetime.now() - startTime)

# # # # # # # # # # #
# Answer: 932718654 #
# Time: 0:00.058    #
# # # # # # # # # # #
