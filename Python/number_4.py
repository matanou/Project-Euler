"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindromic(n):
    if list(str(n))[::-1] == list(str(n)):
        return True
    return False

biggest_so_far = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        if is_palindromic(a*b) and a*b > biggest_so_far:
            biggest_so_far = a*b
            print(biggest_so_far)
