#!/usr/bin/python



import sys
from functools import *
from math import * 
"""
triangle number: T(n) = Sum_i^(n) i



first T(n) to have > 500 divisors (they include 1 and T(n) in the count)

too slow to do trial division for each number, use a prime factorization
then count the combinations to get the number of divisors

To make the factorization easier we use the closed form of the summation:

T(n) = n(n+1)/2      ... this way we factor two numbers on the order of n
                          rather than n^2

                         
"""


import factor
import time


start = time.time()
upto = 30000  
divisor_list = [0,1]
n = 2
while n < upto:
    divisor_list.append(reduce(lambda x,y: x+y, factor.generate_proper_divisors(n)))
    n += 1
# end while

divisor_list_len = len(divisor_list)
print max(divisor_list)

amicable_list = []

for a in range(0,10000):
    b = divisor_list[a]
    if (b >= divisor_list_len):
        continue
    # end if
    if (divisor_list[a] == b and divisor_list[b] == a and a != b):
        if (a not in amicable_list):
            amicable_list.append(a)
        # end if
        if (b not in amicable_list):
            amicable_list.append(b)
        # end if
    # end if
# end for



print amicable_list
print reduce(lambda x, y: x+y, amicable_list)

end = time.time()

print "time:", end - start
#[220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]
#31626


