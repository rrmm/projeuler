#!/usr/bin/python

import sys
from functools import *
from math import * 
"""
triangle number: T(n) = Sum_i^(n) i

there's a closed form solution, but it's easy enough to iteratively keep
track, since we want all the values 

first T(n) to have > 500 divisors (they include 1 and T(n) in the count)

too slow to do trial division for each number, use a prime factorization
then count the combinations to get the number of divisors

"""
c = 0
for i in xrange(1, 76576500):
    if (76576500%i == 0):
        print c,i
        c+=1
    # end if
# end for
print c
# end for
n = (2**5) * (3**2) * 5  * 7 * 11 * 13 * 17 
print n
c = 0
for i in xrange(1, n+1):
    if (n%i == 0):
        print c,i
        c+=1
    # end if
# end for
print c
sys.exit()

def n_is_prime(n, primes):
    for p in primes:
        if (n%p==0):
            return False
        # end if
    # end for
    return True
# end def


primes = []

# for a number of value n, we only need to consider the primes which are 
# less than sqrt(n)
# HOWEVER: we want to consider if the number is prime itself, 
# we could optimize that away since it implies the number only has 
# two divisors (??? this may not work)
def have_enough_primes(n, primes):
    if (len(primes) == 0):
        return False
    # end if
    if (primes[-1] >= n):
        return True
    # end if
    return False
# end def

def generate_more_primes(n, primes):
    if (len(primes) == 0):
        i = 2
    else:
        i = primes[-1] + 1
    # end if
    maxprime = n #sqrt(n) 
    while i <= maxprime:
        if (n_is_prime(i,primes)):
            primes.append(i)
        # end if
        i+=1
    # end while    
# end def


def get_max_pow(n, a):
    # if n = a^i*b, where b is a whole number, returns i
    i = 1
    while n%(a**i)==0:
        i+=1
    # end while
    return i-1
# end def

# ignore 1
def factor(n, primes):
    if (n == 0):
        return [] # corner case
    # end if
    divisors = []
    for i in primes:
        if (n%i == 0):
            exponent = get_max_pow(n,i)
            divisors.append((i, exponent))
        # end if
    # end for
    return divisors
# end for



def create_divisor_list(n, factors):
    # take out for 1 now
    factors = factors[1:]
    print n, factors
# end def


i = 0
count = 0
while i < 10000000:
    i += count
    count+=1 
    if (not have_enough_primes(i, primes)):
        generate_more_primes(i, primes)
    # end if
    factors = factor(i, primes)
    if (factors == []):
        continue
    # end if
    ndivs = reduce(lambda x,y: x*y, [ k+1 for (b,k) in factors ])
    print i, factors, ndivs
    if ndivs > 500:
        break
    # end if
    #len(factors[1:])
    #create_divisor_list(i, divs)
# end while

#c = 0
#for i in range(1, 1000):
#    if (528%i == 0):
#        print i
#        c+=1
#    # end if
# end for
#print c
