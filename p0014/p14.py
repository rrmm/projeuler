#!/usr/bin/python




def seq(x):
    if x%2 == 0:
        return x/2
    else:
        return 3*x+1
    # end if
# end def


def runchain(n):
    seqlen = 1     # include the starting term
    while n != 1:
        n = seq(n)
        seqlen +=1 
    # end while
    return seqlen
# end def

maxlen = 0
maxrun = 0
for i in range(1,int(1e6)):
    r = runchain(i)
    if (r > maxlen):
        maxlen = r
        maxrun = i
    # end if
    if (i%10==0):
        print "@",i, maxlen, maxrun
    # end if
# end for
print maxrun, maxlen

## n = 837799, len = 525
