### Problem 28
### https://projecteuler.net/problem=28

import math
from datetime import datetime
startTime = datetime.now()

def spiral(size):   # spiral dimensions (size x size)
    spiral = [[1]]
    sum  = 0
    for ring in range(1, math.ceil(size / 2)):
        spiral_ring = []
        for n in range(max(spiral[ring - 1]) + 1, max(spiral[ring - 1]) + (8 * ring) + 1):
            spiral_ring.append(n)
        spiral.append(spiral_ring)
    
    for i in range(1, len(spiral)):
        for n in range((len(spiral[i]) // 4) - 1, len(spiral[i]), len(spiral[i]) // 4):
            sum += spiral[i][n]

    return sum + 1, len(spiral)

print(spiral(1001))
print(datetime.now() - startTime)

# # # # # # # # # # #
# Answer: 669171001 #
# Time: 0:00.170    #
# # # # # # # # # # #
