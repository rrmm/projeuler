#!/usr/bin/python

# sum of digits of 2**1000

n = 2**1000
sum = 0
while n > 0:
    i = n%10
    n /= 10
    sum += i
    print n
# end while
print sum
