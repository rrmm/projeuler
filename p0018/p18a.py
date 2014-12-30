#!/usr/bin/python

t0 = """3
7 4
2 4 6
8 5 9 3
"""
t1 = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def read_triangle(triangle):
    tt = triangle.strip().split('\n')
    res = []
    for r in tt:
        res.append([ int(i) for i in r.split(' ')])
    # end for
    return res
# end def


it = read_triangle(t1)

for i in range(len(it)-2,-1,-1):
    for j in range(0,len(it[i])):
        pv = it[i+1][j]
        nv = it[i+1][j+1]
        it[i][j] = it[i][j]+max(pv,nv)
        #print it[i][j], pv, nv
    # end for
    #print 
# end for 
print "max:", max(it[0])
