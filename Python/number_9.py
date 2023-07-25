"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

                                                    a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math


values_before = []
for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt(a**2 + b**2)
        if a + b + c == 1000:
            lst_abc = [a, b, c]
            lst_abc.sort()
            if lst_abc not in values_before:
                print(a, b, c, a * b * c)
                values_before.append(lst_abc)
