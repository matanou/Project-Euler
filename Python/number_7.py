"""
https://projecteuler.net/problem=7

By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10_001st prime number?
"""

n = 3
i = 0

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

while i != 10_002:
    if is_prime(n):
        i += 1
    n += 2

print(n)
