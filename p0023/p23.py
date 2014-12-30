#!/usr/bin/python


import factor
from functools import reduce


# returns negative for deficient numbers, 0 for perfect ones
# positive for abundant
def check_num(n):
    factors = factor.generate_proper_divisors(n)
    if (len(factors) == 0):
        return 0
    # end if
    res = reduce(lambda x,y: x+y, factors)
    return res - n
# end def


abundant = []
maxnum = 28123
for i in range(2, maxnum+1):
    res = check_num(i)
    if (res > 0):
        abundant.append(i)
    # end if
# end for

#print abundant

# sums of pairs of abundant numbers, only add them once
abundant_sums = {}
for i in abundant:
    for j in abundant:
        abundant_sums[(i+j)] = 1
    # end for
# end for


# sum of the sums of two abundant numbers
total_of_sums_of_abundant = 0
for i in abundant_sums.keys():
    if (i <= maxnum):
        total_of_sums_of_abundant += i
    # end if
# end for




print maxnum*(maxnum+1)/2 - total_of_sums_of_abundant

# answer: 4179871
