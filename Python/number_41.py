"""
https://projecteuler.net/problem=41 

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import math


def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_pandigital(n):
    lst_num = list(str(n))
    if len(lst_num) == 10:
        if "0" in lst_num and "1" in lst_num and "2" in lst_num and "3" in lst_num and "4" in lst_num and "5" in lst_num and "6" in lst_num and "7" in lst_num and "8" in lst_num and "9" in lst_num:
            return True
    return False

def generate_all_possible_arrangement_of(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]

        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in generate_all_possible_arrangement_of(remLst):
            l.append([m] + p)
    return l

list_of_pandigital = generate_all_possible_arrangement_of([1, 2, 3, 4, 5, 6, 7])

print(len(list_of_pandigital))

for i in list_of_pandigital:
    new_list = [str(current_integer) for current_integer in i]
    string_value = "".join(new_list)
    number = int(string_value)
    if is_prime(number):
        print(number)
