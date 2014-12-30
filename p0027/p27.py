#!/usr/bin/python


import factor


test_primes = factor.get_primes_upto(2000)
primes = [ i for i in test_primes if i < 1000]

def f(n, a, b):
    return n*n + a * n + b
# end def

primes = primes[1:]


neg_primes = [ -x for x in primes ]
primes = neg_primes + primes 
# print primes

# f(n, a, b) = n^2 + a*n + b
# 1. for f(0, a, b) to be prime, requires b to be prime
# 2. if we exclude the prime 2, then for f(1, a, b) to be prime
#       a must be odd, 1+a+b, 1+odd+odd == 1+even == odd
# 
# handle the prime 2 separately
#

argmax = -1
valmax = -1

for b in primes:
    for a in range(-999,1000,2):
        #n0 = f(0,a,b)
        j = 0
        while 1:
            n1 = f(j,a,b)
            res = n1 in test_primes
            if (not res):
                if (j > argmax):
                    argmax = j
                    valmax = (a,b)
                # end if
                break
            # end if
            j += 1
        # end while
    # end for a
# end for b


print valmax, argmax, valmax[0]*valmax[1]
# (-61, 971) 71
