"""
The number, 1_406_357_289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.
Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

 - d2d3d4 = 406 is divisible by 2
 - d3d4d5 = 063 is divisible by 3
 - d4d5d6 = 635 is divisible by 5
 - d5d6d7 = 357 is divisible by 7
 - d6d7d8 = 572 is divisible by 11
 - d7d8d9 = 728 is divisible by 13
 - d8d9d10 = 289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import math

# 1 Generate all the 0 to 9 pandigital
# 2 Check if they satisfy THE property

# 1
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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

#2
def proprerty(n):
    if int(str(n[1]) + str(n[2]) + str(n[3])) % 2 == 0:
        if int(str(n[2]) + str(n[3]) + str(n[4])) % 3 == 0:
            if int(str(n[3]) + str(n[4]) + str(n[5])) % 5 == 0:
                if int(str(n[4]) + str(n[5]) + str(n[6])) % 7 == 0:
                    if int(str(n[5]) + str(n[6]) + str(n[7])) % 11 == 0:
                        if int(str(n[6]) + str(n[7]) + str(n[8])) % 13 == 0:
                            if int(str(n[7]) + str(n[8]) + str(n[9])) % 17 == 0:
                                return True
    return False

def translate_lst_to_int(lst):
    str_n = ""
    for i in lst:
        str_n += str(i)
    print(int(str_n))
    return int(str_n)

sum_ = 0
for p in generate_all_possible_arrangement_of(digits):
    if proprerty(p):
        print(translate_lst_to_int(p))
        sum_ += translate_lst_to_int(p)
print(sum_)
