#!/usr/bin/python

from math import *


base20 = [ "",
          "one",
          "two",
          "three",
          "four",
          "five",
          "six",
          "seven",
          "eight",
          "nine",
          "ten",
          "eleven",
          "twelve",
          "thirteen",
          "fourteen",
          "fifteen",
          "sixteen",
          "seventeen",
          "eighteen",
          "nineteen" ]


tens = [ "",
         "",
         "twenty",
         "thirty",
         "fourty",
         "fifty",
         "sixty",
         "seventy",
         "eighty",
         "ninety",
         ""]
         

units = [ "",
          "hundred",
          "thousand",
          "million",
          "billion",
          "trillon"]          


# do the simplest thing that works, in that vein, we special-case 1000
# we could do this more generally, by having a units routine
# for numbers above 100
def get_number_word(i):
    o = i%10
    tw = i%20    
    t = (i/10)%10
    h = (i/100)%10
    th = i - i%1000
    if (i%100 > 19):
        pt = tens[t]
        if (base20[o] != ""):
            pt +="-"+base20[o]
        # end if
    else:
        pt = base20[tw]
    # end if
    if (i%1000 > 99):
       ph = base20[h]+" hundred "
       if (i%1000 > 100):
           ph += "and "
       # end if
    else:
       ph = ""
    # end if
    if (i == 1000):
        return "one thousand"
    else:
        return ph+pt
    # end if
    
# end def


count = 0
for i in range(1,1001):
    s = get_number_word(i)
    s = s.replace(" ", "") # don't count spaces or hyphens
    s = s.replace("-", "") 
    count += len(s)
# end for

print count
