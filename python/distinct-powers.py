### Problem 29
### https://projecteuler.net/problem=29

from datetime import datetime
startTime = datetime.now()

def sequence(a_max, b_max):
    terms = set()
    for i in range(2, a_max + 1):
        for j in range(2, b_max + 1):
            terms.add(i ** j)

    return len(terms)

print(sequence(100, 100))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 9183    #
# Time: 0:00.006  #
# # # # # # # # # #
