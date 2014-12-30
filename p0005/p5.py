#!/usr/bin/python

#
# what is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?
#
# do it by hand is quick given the problem size
# otherwise factor, then take the max power of each factor


#the prime numbers from 1 to 20 are 
primes = [ 2,3,5,7,11,13,17,19 ]
ns = [ 2, 3, 2*2,5,2*3,7,2*2*2,3*3,2*5,11,2*2*3,13,2*7,3*5,2*2*2*2,17,2*3*3,19,2*2*5 ]
# powers
nsp = [ (1,0,0,0,0,0,0,0), 
        (0,1,0,0,0,0,0,0), 
        (2,0,0,0,0,0,0,0),
        (0,0,1,0,0,0,0,0),
        (1,1,0,0,0,0,0,0),
        (0,0,0,1,0,0,0,0),
        (3,0,0,0,0,0,0,0),
        (0,2,0,0,0,0,0,0),
        (1,0,1,0,0,0,0,0),
        (0,0,0,0,1,0,0,0),
        (2,1,0,0,0,0,0,0),
        (0,0,0,0,0,1,0,0),
        (1,0,0,1,0,0,0,0),
        (0,1,1,0,0,0,0,0),
        (4,0,0,0,0,0,0,0),
        (0,0,0,0,0,0,1,0),
        (1,2,0,0,0,0,0,0),
        (0,0,0,0,0,0,0,1),
        (2,0,1,0,0,0,0,0)]
cmax =  (4,2,1,1,1,1,1,1)
res = (2**4) * (3**2) * 5 * 7 * 11 * 13 * 17 * 19


for i in range(1,21):
    print res%i
# end for




