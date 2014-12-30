#!/usr/bin/python

import sys

s = [ 0,1,2,3,4,5,6,7,8,9 ]

def brute_perm(count, prefix, left):
    if len(prefix) == 10:
        if count == 1e6-1:
            print count, prefix
        # end if
        return count+1
    # end if    
    for i in range(0, len(left)):
        m = left[i]
        count = brute_perm(count, prefix+str(m),[ n for n in left if n != m])  
    # end for
    return count
# end def

from math import factorial as fact

def nthpermgen(left, nth):
    if (left == []):
        return ""
    # end if
    left.sort() # make sure they are in lexicographic order
    l = fact(len(left)-1)
    rem = nth%l
    m = left[nth/l]
    return str(m) + nthpermgen([ n for n in left if n != m], rem)
# end def

print nthpermgen(s, int(1e6-1))

sys.exit()
brute_perm(0, "",s)

# 999999 2783915460
