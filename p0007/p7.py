#!/usr/bin/python

"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

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
# we make a guess here about the maxvalue and raise it as necessary
# so the run remains quick
maxprime = sqrt(200000)
primes = []

while 1:
    if (n_is_prime(n,primes)):
        count+=1
        #print count
        if (n < maxprime):
            primes.append(n)
        # end if
    # end if
    # print count,primes
    n+=1
    if (count == 10001):
        print "10001st prime is", n
        print "maxprime tested was",maxprime,"; sqrt(n) is",sqrt(n)
        break
    # end if
# end while

