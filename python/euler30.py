### Problem 30
### https://projecteuler.net/problem=30

from datetime import datetime
startTime = datetime.now()

def digit_power_sum(power):
    sum = 0
    n = 2
    while True:
        number_string = str(n)
        string_sum = 0
        if (9 ** power) * len(number_string) < n:
            break
        for i in range(0, len(number_string)):
            string_sum += int(number_string[i]) ** power
        if n == string_sum:
            print(n)
            sum += string_sum
        n += 1

    return sum

print(digit_power_sum(5))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 443839  #
# Time: 0:01.060  #
# # # # # # # # # #
