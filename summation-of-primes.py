# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

integers = set()

def prime_sum(limit):
    for i in range(2, limit):
        integers.add(i)
            
    return integers

print(sorted(prime_sum(100)))