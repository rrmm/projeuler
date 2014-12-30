#!/usr/bin/python




def get_neighbors(loc, size):
    res = [ (loc[0]+1,loc[1]), 
            #(loc[0]-1,loc[1]),   # these can never be taken in the problem 
            (loc[0],loc[1]+1),
            #(loc[0],loc[1]-1)
            ]
    res = filter(lambda x: x[0] >= 0 and x[1] >= 0 and x[0] < size[0] and x[1] < size[1], res)
    return res
# end def

vertex_count_cache = {}

def traverse(level, vertex, cache, new_cache, size):

    if (vertex in cache):
        return cache[vertex]
    # end if

    neighbor_lst = get_neighbors(vertex, size)
    #print " "*level, vertex, neighbor_lst
    count = 0
    if (vertex == (size[0]-1, size[1]-1)):
        return 1
    # end if
    
    for n in neighbor_lst:
        if (n[0] < vertex[0] or n[1] < vertex[1]):
            continue
        # end if
        
        count += traverse(level + 1, n, cache, new_cache, size)
    # end for
    if (vertex[0] == 0 or vertex[1] == 0):
        # store it for the next problem
        new_cache[(vertex[0]+1), (vertex[1]+1)] = count
    # end if
    return count
# end def


# too slow to do directly
# we can do a memoized/divide and conquer/dynamic programming solution

cache = {}
new_cache = {}

for i in range(3, 22):
    print traverse(0, (0,0), cache, new_cache, (i,i))
    cache = new_cache
    new_cache = {}
# end for


# should be the same as, since it's basically pascal's triangle
from math import factorial as fact
print fact(40)/(fact(20)*fact(20))
