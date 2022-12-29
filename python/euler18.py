### Problem 18
### https://projecteuler.net/problem=18

from datetime import datetime
startTime = datetime.now()

def pathSum(strTriangle):
    list = []
    triangle = []
    rmBreak = strTriangle.replace("\n", "")   # remove line breaks from strTriangle
    strTriangle = rmBreak
    rmSpace = strTriangle.replace(" ", "")   # remove spaces from strTriangle
    strTriangle = rmSpace

    for i in range(0, len(strTriangle), 2):   # create list of integers from strTriangle slices
        if strTriangle[i] == "0":
            list.append(int(strTriangle[i+1:i+2]))
        else:
            list.append(int(strTriangle[i:i+2]))

    for i in range(1, len(list)):   # create triangle from list slices
        if list[0:i] == []:
            break
        triangle.append(list[0:i])
        del list[0:i]

    for i in range(len(triangle)-2, -1, -1):   # find maximum path sum from bottom to top by combining second to last row values with largest adjacent values below
        collapse = []
        for j in range(0, len(triangle[i])):
            if triangle[i][j] + triangle[i+1][j] > triangle[i][j] + triangle[i+1][j+1]:
                collapse.append(triangle[i][j] + triangle[i+1][j])
            else:
                collapse.append(triangle[i][j] + triangle[i+1][j+1])
        triangle[i] = collapse
        del triangle[i+1]
    print(triangle[0][0])

pathSum(open("input/fifteen-row-triangle.txt").read())
print(datetime.now() - startTime)

# # # # # # # # # # 
# Answer: 1074    #
# Time: 0:00.001  #
# # # # # # # # # #
