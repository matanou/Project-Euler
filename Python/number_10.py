"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time

n = 3

frequent_factors = [2]


def is_pseudo_prime(n):  # "pseudo_prime" because the numbers passing this function and return True,
                         # have a very high probability of being prime but have less and less chance
                         # of being prime if they get bigger.
    for i in frequent_factors:
        if n % i == 0 and n != i:
            return False
    if n not in frequent_factors and n <= 1_409:  # 1409 is the best value I could come with to make things
                                                  # as fast as possible.
        frequent_factors.append(n)
    return True


sum = 2  # as 2 is a prime number and it makes the calculations faster to make
         # to have all the numbers that are looked at to be odd.
while n < 2_000_000:
    if is_pseudo_prime(n):
        sum += n
    n += 2

print(sum)
