#!/usr/bin/python


from math import sqrt


fib = (1,1)
for i in range(0, 100000):
    fib = (fib[1], fib[0]+fib[1])
    if (len(str(fib[1])) >= 1000):
        print len(str(fib[1])),fib[1]
        break
    # end if
# end for


