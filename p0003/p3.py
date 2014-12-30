#!/usr/bin/python

from functools import reduce

# find the prime numbers
# we could use: sieve of eratosthenes (with optimizations), incremental seive,
#   or trial division

# we do a simple trial division until we find all the primes
# to be added to the set of primes, the new number has to be 
# relatively prime to all the primes currently on the list 


n = 600851475143
#n = 13195



def multiplyList(lst):
    if (lst == []):
        return 0
    # end if
    return reduce(lambda x,y: x*y, lst)
# end def

def isRelativePrime(n, lst):
    res = [ n%i==0 for i in lst ]
    print res
    if True in res:
        return False
    else:
        return True
    # end if
# end def

pfact = []
for i in xrange(2,n):
    if (n%i == 0):
        if (isRelativePrime(i, pfact)):
            pfact.append(i)
            #check to see if we've found all factors
            # this only works if there are no repeated factors
            # but works in this case
            value = multiplyList(pfact)
            if (value == n):
                break 
            # end if
        # end if
    # end if
# end for
print pfact
print max(pfact)
