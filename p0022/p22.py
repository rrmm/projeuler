#!/usr/bin/python


f = open("names.txt")
names = f.read().replace('"', '').split(',')
names.sort()


def calc_value(s):
    acc = 0
    for c in s:
        acc += ord(c)-ord('A') + 1
    # end for
    return acc
# end def




count = 1
total = 0
for name in names:
    v = calc_value(name)
    #if (name == "COLIN"):
    #   print count, v
    # end if
    total += count*v
    count += 1
# end for

print total  
# should be 871198282
