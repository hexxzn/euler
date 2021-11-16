# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

prime_list = [2, 3, 5]
prime = 0
max = 2000000
x = 1


while prime < max:
    prime = (6 * x) + 1
    if prime < max:
        prime_list.append(prime)

    prime = (6 * x) - 1
    if prime < max:
        prime_list.append(prime)

    x += 2

prime_list = list(set(prime_list))   # eliminate duplicates
prime_list.sort()
print("Primes:", prime_list)
print("Sum:", sum(prime_list))