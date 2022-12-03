"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (5) = 10.
                                       (3)

In general, (n) = n!/(r!*(n-r)!), where r <= n,n!.
            (r)

It is not until n = 23, that a value exceeds one-million: (23) = 1144066.
                                                          (10)

How many, not necessarily distinct, values of (n) for 1 <= n <= 100, are greater than one-million?
                                              (r)
"""


import math


def r_from_n(r, n):
    if r <= n and r <= math.factorial(n):
        n_fact = math.factorial(n)
        r_fact = math.factorial(r)
        n_r_fact = math.factorial((n-r))
        result = n_fact/(r_fact*n_r_fact)
        return result


count = 0
n = 1
while n <= 100:
    for r in range(n):
        print(r, n)
        if r_from_n(r, n) > 1_000_000:
            count += 1
    n += 1

print(count)
