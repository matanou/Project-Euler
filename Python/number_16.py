"""
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8.

What is the sum of the digits of the number 2^1000?
"""

liste = list(str(2**1000))
sum_ = 0

for i in liste:
    sum_ += int(i)

print(sum_)
