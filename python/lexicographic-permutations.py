### Problem 24
### https://projecteuler.net/problem=24

from datetime import datetime
import itertools
startTime = datetime.now()

def permutations(digits):
    lstTemp = list(itertools.permutations(i for i in range(digits)))
    lstPermutations = []
    for i in range(len(lstTemp)):
        permutation = ""
        for j in range(digits):
            permutation += str(lstTemp[i][j])
        lstPermutations.append(permutation)
        if len(lstPermutations) == 1000000:
            lstPermutations.sort(key = int)
            return lstPermutations[999999]

print(permutations(10))
print(datetime.now() - startTime)

# # # # # # # # # # # #
# Answer: 2783915460  #
# Time: 0:03.503      #
# # # # # # # # # # # #
