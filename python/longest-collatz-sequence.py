### Problem 141
### https://projecteuler.net/problem=14

from datetime import datetime
startTime = datetime.now()

def sequence(limit):
    dict = {}   # dictionary key = starting number, value = chain length
    for i in range(1, limit):
        dict[i] = 1   # each starting number begins with chain length of 1 which represents the starting number itself (i)
        n = i   # using n for math operations so that i can be referenced as dictionary key
        while n != 1:
            if n / 2 in dict.keys():   # if n/2 exists in dictionary, add n/2's chain length to current chain length and skip remainder of sequence (IMPORTANT)
                dict[i] += dict[n/2]
                break
            elif n % 2 == 0:   # if n is even, generate next n in sequence, add 1 to chain length
                n = n / 2
                dict[i] += 1
            else:   # if n is odd, generate next n in sequence, add 1 to chain length
                n = (3 * n) + 1
                dict[i] += 1
    return max(dict, key=dict.get)

print(sequence(1000000))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 837799  #
# Time: 0:03.264  #
# # # # # # # # # #
