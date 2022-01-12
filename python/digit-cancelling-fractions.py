### Problem 33
### https://projecteuler.net/problem=33

from decimal import *
from datetime import datetime
startTime = datetime.now()

product = 1
for denominator in range(10, 100):
    for numerator in range(10, denominator):
        numerator_string = str(numerator)
        denominator_string = str(denominator)
        for n_char in numerator_string:
            for d_char in denominator_string:
                if n_char == d_char and n_char != "0":
                    new_numerator = numerator_string.replace(n_char, "")
                    new_denominator = denominator_string.replace(d_char, "")
                else:
                    continue
                if new_denominator != "" and new_numerator != "" and new_denominator != "0":
                    result = (int(new_numerator) / int(new_denominator))
                    if result == numerator / denominator:
                        product *= (result * 10)

print(int(product))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 100     #
# Time: 0:00.007  #
# # # # # # # # # #
