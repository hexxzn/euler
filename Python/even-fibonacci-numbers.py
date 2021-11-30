### Problem 2
### https://projecteuler.net/problem=2

from datetime import datetime
startTime = datetime.now()

fibonacci1 = 1      # previous term in sequence
fibonacci2 = 2      # current term in sequence
fibonacci3 = 0      # placeholder
sum = 0             # sum of even-valued terms

while fibonacci2 < 4000000:
    if fibonacci2 % 2 == 0:
        sum += fibonacci2
    fibonacci3 = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 = fibonacci3

print(sum)
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 4613732 #
# Time: 0:00.001  #
# # # # # # # # # #
