#!/usr/bin/python

from functools import reduce


"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# we can do this through brute force and ignorance 

for a in range(0,1001):
    arem = 1000-a
    for b in range(0,arem):
        c = 1000-a-b
        if (a**2+b**2 == c**2 and a < b and b < c):
            print a,b,c,a+b+c
        # end if
    # end for
# end for
