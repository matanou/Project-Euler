"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def find_factors(n):
    for i in range(3, n, 2):
        if n % i == 0 and is_prime(i):
            print(i)
            # should be running for a while but won't print a value higher than 6857 (which is the answer)

find_factors(600851475143)
