### Problem 14
### https://projecteuler.net/problem=14

from datetime import datetime
startTime = datetime.now()

def sequence(limit):
    dict = {}
    for i in range(1, limit):
        dict[i] = 1
        n = i
        while n != 1:
            if n / 2 in dict.keys():
                dict[i] += dict[n/2]
                break
            elif n % 2 == 0:
                n = n / 2
                dict[i] += 1
            else:
                n = (3 * n) + 1
                dict[i] += 1
    return max(dict, key=dict.get)

print(sequence(1000000))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 837799  #
# Time: 0:03.264  #
# # # # # # # # # #
