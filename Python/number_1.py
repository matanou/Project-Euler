"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

n = 1

sum = 0
while n < 1000:
    if n % 15 == 0:
        print(n)
        sum += n
    elif n % 3 == 0 and n % 5 != 0:
        print(n)
        sum += n
    elif n % 3 != 0 and n % 5 == 0:
        print(n)
        sum += n

    n += 1

print(sum)
