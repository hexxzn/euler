# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

integers = [2]
prime = 2
cap = 200
var = True

for i in range(3, cap, 2):
    integers.append(i)

while var is True:
    for i in range(prime, max(integers), 2):
        nonprime = i * prime
        if nonprime > max(integers):
            break
        elif nonprime in integers:
            integers.remove(nonprime)

    # print(prime)

    if integers.index(prime) + 1 < len(integers):
        prime = integers[integers.index(prime) + 1]
    else:
        break

print(integers)
