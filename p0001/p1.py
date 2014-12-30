#!/usr/bin/python


c = 0
for i in range(0,1000):
    if (i%3 == 0) or (i%5 == 0): 
        #print i
        c+=i 
    # end if
# end for

print("sum of multiples of 3 or 5 in interval (0,1000): %i"%c)
