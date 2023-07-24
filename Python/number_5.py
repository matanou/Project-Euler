"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""

n = 20

def is_divisible_by_all_from(a, b, n):
    for k in range(a, b+1):
            if n % k != 0:
                return False
    return True

print(is_divisible_by_all_from(1, 10, 2520))

while not is_divisible_by_all_from(1, 20, n):
    n += 1

# it takes a very long time to find the answer (I haven't found a way of making it faster) but it does find the correct answer
print(n)
