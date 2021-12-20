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

    for i in range(len(triangle)-2, -1, -1):   # find maximum path sum by from bottom to top by combining second to last row values with largest adjacent values below
        collapse = []
        for j in range(0, len(triangle[i])):
            if triangle[i][j] + triangle[i+1][j] > triangle[i][j] + triangle[i+1][j+1]:
                collapse.append(triangle[i][j] + triangle[i+1][j])
            else:
                collapse.append(triangle[i][j] + triangle[i+1][j+1])
        triangle[i] = collapse
        del triangle[i+1]
    print(triangle[0][0])

pathSum("""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""")
print(datetime.now() - startTime)

# # # # # # # # # # 
# Answer: 1074    #
# Time: 0:00.001  #
# # # # # # # # # #
