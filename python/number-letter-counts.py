### Problem 171
### https://projecteuler.net/problem=17

from datetime import datetime
startTime = datetime.now()

def letter_count(exp):
    ones = {1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    tens = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
    numstring = "onethousand"

    for i in range(1, exp + 1):
        number = i
        digits = [int(a) for a in str(number)]
        if len(digits) == 3:   # hundreds
            output = ones[digits[0]] + "hundred"
            if digits[1] == 0 and digits[2] == 0:
                numstring += output
            elif digits[1] != 0 and digits[2] == 0:
                if digits[1] == 1:
                    output += "and" + teens[10]
                    numstring += output
                else:
                    output += "and" + tens[digits[1]]
                    numstring += output
            elif digits[1] == 0 and digits[2] != 0:
                output += "and" + ones[digits[2]]
                numstring += output
            else:
                if digits[1] == 1:
                    output += "and" + teens[int(str(digits[1])+str(digits[2]))]
                    numstring += output
                else:
                    output += "and" + tens[digits[1]] + ones[digits[2]]
                    numstring += output
        elif len(digits) == 2:   # tens
            if digits[0] == 1:
                output = teens[int(str(digits[0])+str(digits[1]))]
                numstring += output
            elif digits[1] == 0:
                output = tens[digits[0]]
                numstring += output
            else:
                output = tens[digits[0]] + ones[digits[1]]
                numstring += output
        elif len(digits) == 1:   # ones
            output = ones[digits[0]]
            numstring += output

    return(len(numstring))

print(letter_count(1000))
print(datetime.now() - startTime)

# # # # # # # # # # 
# Answer: 21124   #
# Time: 0:00.003  #
# # # # # # # # # #
