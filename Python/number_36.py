"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import math
n = 1
sumation = 0

# the recursive function to reverse
def rev(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10))
def is_palindrome(n):
    if n == rev(n):
    	return True
    else:
    	return False

   


while n <= 1_000_000:
  binary_n = int("{0:b}".format(n))
  
  if is_palindrome(n):
    if is_palindrome(binary_n):
      sumation += n
      print(n, "is palindrome !")
  n += 1

print(sumation)

  
