### Problem 21
### https://projecteuler.net/problem=2

from datetime import datetime
startTime = datetime.now()

def evensum(limit):
    sequence = [1, 2]
    sum = 0

    while sequence[-1] < limit:
        sequence.append(sequence[-1] + sequence[-2])

    if sequence[-1] > limit:
        del sequence[-1]

    for element in sequence:
        if element % 2 == 0:
            sum += element

    return sum

print(evensum(4000000))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 4613732 #
# Time: 0:00.001  #
# # # # # # # # # #
