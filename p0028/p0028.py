#!/usr/bin/python


#
#        s_{n-1}^2 + 3*(s_n - 1)  ...       s_n^2
#                 ...              .         ...
#        s_{n-1}^2 + 2*(s_n - 1)  ...    s_{n-1}^2 + s_n - 1
#
# s = 1,3,5,7,...
#
# 3*(s-2)**2 + 6*(s - 1) + s**2
#
# 3*(s^2 - 4s + 4) + 6s - 6 + s^2
# 3*s^2 - 12s+12 + 6s - 6 + s^2
# 4*s^2 - 6*s + 6
#  
# switch the formula to rescale 3,5,...,1001 to 1,2,3,...500
# s = 2*i + 1
# 4*(4*i^2 + 4i + 1) - 12*i - 6 + 6
# 16*i^2 + 16i + 4 - 12*i - 6 + 6
# 16*i^2 + 4*i + 4
# 
# do the closed form of the sum
# 1 + sum_{i=1}^{500}  { 16*i^2 + 4*i + 4 }
# n = 500
# 16*(2*n*n*n + 3*n*n + n)/6 + 4*(n^2 + n/2)/2 + 4*500
n = 500
print 1+ 16*(2*n*n*n + 3*n*n + n)/6 + 4*(n*n + n)/2 + 4*n

acc = 1  # starting from len 3 sides
for i in range(1,501):
    acc += 16*i*i + 4*i + 4  # 3*(s-2)**2 + 6*(s - 1) + s**2
    #print i, acc
# end for

print acc
