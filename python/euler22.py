### Problem 22
### https://projecteuler.net/problem=22

from datetime import datetime
startTime = datetime.now()

txtNames = open("input/names.txt", "r").read()
lstNames = (txtNames.replace("\"", "")).split(",")
lstNames.sort()

txtAlphabet = open("input/alphabet.txt", "r").read()
lstAlphabet = txtAlphabet.split(",")

def namesScores():
    score_total = 0
    for i in range(len(lstNames)):
        score = 0
        for letter in lstNames[i]:
            score += lstAlphabet.index(letter) + 1
        score = score * (lstNames.index(lstNames[i]) + 1)
        score_total += score
    return score_total

print(namesScores())
print(datetime.now() - startTime)

# # # # # # # # # # #
# Answer: 871198282 #
# Time: 0:00.153    #
# # # # # # # # # # #
