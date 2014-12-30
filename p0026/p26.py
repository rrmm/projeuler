#!/usr/bin/python

import factor

def div(x,d):
    lst = []
    div_lst = []
    initial = d
    x*=10      # take off the 0 before the decimal 
    while 1:
        while (x//d < 1):
            x *= 10
            lst.append(int(0))
            div_lst.append(0)   # just to keep the count accurate later on
        # end while
        digit = x//d
        rem = int(x%d)

        lst.append(int(digit))
        if (rem == 0):
            break 
        else:
            x = rem
        # end if
        x *= 10
        if (rem in div_lst):
            #print "here", initial, len(div_lst)-div_lst.index( rem)
            #print rem
            # print "".join([ str(i) for i in lst])
            #print div_lst
            return len(div_lst)-div_lst.index(rem)
        # end if
        div_lst.append((rem))
    # end while
    #print "".join([ str(i) for i in lst])
    #print div_lst
    return 0
# end def


# using fermat's little theorem
# a^(p-1) = 1 (mod p)
# 10^x == 1 (mod p) 
def get_order(n):
    i = 1
    factors = factor.factor(n)
    # ignore the non-prime numbers
    if (factors[0][0] != n):
        return -1
    # end if
    while 1:
        if (((10**i)%n) == 1):
            break
        # end if
        i+=1 
    # end 
    return i
# end def

argmax = 0
maxlen = 0
for i in range(11, 1000):
    l = div(1.0,i)
    maxlen = max(l, maxlen)
    if (maxlen == l):
        argmax = i
    # end if
    print i, l, get_order(i)
# end def

print argmax, maxlen
