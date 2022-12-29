### Problem 31
### https://projecteuler.net/problem=31

from datetime import datetime
startTime = datetime.now()

def coin_combinations(target_sum):
    combinations = 1
    for one_pound in range(0, 2 + 1):
        one_pound_sum = one_pound * 100
        for fifty_pence in range(0, 4 + 1):
            fifty_pence_sum = fifty_pence * 50
            for twenty_pence in range(0, 10 + 1):
                twenty_pence_sum = twenty_pence * 20
                for ten_pence in range(0, 20 + 1):
                    ten_pence_sum = ten_pence * 10
                    for five_pence in range(0, 40 + 1):
                        five_pence_sum = five_pence * 5
                        for two_pence in range(0, 100 + 1):
                            two_pence_sum = two_pence * 2
                            temp_sum = two_pence_sum + five_pence_sum + ten_pence_sum + twenty_pence_sum + fifty_pence_sum + one_pound_sum
                            if temp_sum > target_sum:
                                break
                            for one_pence in range(0, 200 + 1):
                                one_pence_sum = one_pence
                                sum = one_pence_sum + two_pence_sum + five_pence_sum + ten_pence_sum + twenty_pence_sum + fifty_pence_sum + one_pound_sum
                                if sum > target_sum: 
                                    break
                                if sum == target_sum:
                                    combinations += 1
    return combinations

print(coin_combinations(200))
print(datetime.now() - startTime)

# # # # # # # # # #
# Answer: 73682   #
# Time: 0:01.185  #
# # # # # # # # # #
