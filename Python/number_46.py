"""
https://projecteuler.net/problem=46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

odd = 3

def list_primes(n):
    liste_primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            liste_primes.append(i)

    return liste_primes

def is_Goldbach(n):
    for prime in list_primes(n + 1):
        for i in range(n + 1):
            value = prime + 2*(i**2)
            if value == n:
                print(f"{n} = {prime} + 2*{i}^2")
                return True


while is_Goldbach(odd):
    odd += 2

print(odd)
