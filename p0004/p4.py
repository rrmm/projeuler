#!/usr/bin/python

#
# Find the largest palindrome made from the product of two 3-digit numbers.
#

a,b,c = (1,3,5)
x,y,z = (1,2,3)

A = a*100+b*10+c
X = x*100+y*10+z

def isPalindrome(a,b,c, x,y,z):
    x0 = (z*c) % 10
    x1 = ((z*c)//10 + (z*b + y*c))%10
    x2 = (((z*c)//10 + (z*b + y*c))//10 + (z*a + y*b + x*c)) % 10
    x3 = ((((z*c)//10 + (z*b + y*c))//10 + (z*a + y*b + x*c)) //10 + (y*a + x*b))%10
    x4 = (((((z*c)//10 + (z*b + y*c))//10 + (z*a + y*b + x*c)) //10 + (y*a + x*b))//10 + x*a)%10
    x5 = ((((((z*c)//10 + (z*b + y*c))//10 + (z*a + y*b + x*c)) //10 + (y*a + x*b))//10 + x*a))//10
    if (x5 == 0 and x0==x4 and x1==x3):
        return True
    if (x0==x5 and x1==x4 and x2==x3):
        return True
    return False
# end def

largest = (0,0,0) # this is i*j, i, j
for i in range(100,1000):
    for j in range(100,1000):
        v = i*j
        res = isPalindrome(i//100,(i//10)%10,i%10, 
                           j//100,(j//10)%10,j%10)
        if (res):  
            print "palindrome:",i*j
            if (v > largest[0]):
                largest = (i*j, i, j)
            # end if
        # end if
    # end for
# end for

print largest
#print (A*X)
#print (x5,x4,x3,x2,x1,x0)


