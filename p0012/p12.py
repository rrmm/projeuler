#!/usr/bin/python

import sys
import time
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



start = time.time()
n = 0
while 1:
    i = n*(n+1)/2
    factors0 = factor.factor(n)    
    factors1 = factor.factor(n+1)    
    factors = factor.merge_factor_list(factors0, factors1)
    # remove a factor of two since we divide by 2 in the formula
    # we know the number has a factor of two at this point since it is even*odd
    factor.remove_factor_from_list(factors, (2, 1))
    if (factors == []):
        n+=1
        continue
    # end if

    ndivs = reduce(lambda x,y: x*y, [ k+1 for (b,k) in factors ])
    print i, factors, ndivs
    if ndivs > 500:
        break
    # end if
    n += 1
# end while
end  = time.time()

print end-start

sys.exit()
c = 0
for i in range(1, 76576500):
    if (76576500%i == 0):
        print i
        c+=1
    # end if
# end for
print c
