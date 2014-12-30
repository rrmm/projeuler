#!/usr/bin/python

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from math import sqrt

def n_is_prime(n, primes):
    for p in primes:
        if (n%p==0):
            return False
        # end if
    # end for
    return True
# end def

n = 2
count = 0
# for a number of value n, we only need to consider the primes which are 
# less than sqrt(n)
max_n = 2000000
maxprime = sqrt(max_n)
primes = []
primesum = 0
while n < max_n:
    if (n_is_prime(n,primes)):
        primesum+=n
        #print n
        if (n < maxprime):
            primes.append(n)
        # end if
    # end if
    # print count,primes
    n+=1
# end while

# 142913828922 
print primesum
