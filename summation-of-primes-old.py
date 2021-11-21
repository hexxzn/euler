# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

integers = [2, 3]
prime = 3
cap = 200

for i in range(5, cap, 2):   # create starter list
    integers.append(i)

while True:
    for i in range(prime, max(integers), 2):   # remove non-prime integers
        nonprime = i * prime
        if nonprime > max(integers):
            continue
        elif nonprime in integers:
            integers.remove(nonprime)

    # print(prime)

    if integers.index(prime) + 1 < len(integers):
        prime = integers[integers.index(prime) + 1]
    else:
        break

print(integers)
print("Sum:", str(sum(integers)))
