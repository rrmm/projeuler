#!/usr/bin/python



def isLeapYear(y):
    return y%4==0 and (y%100 != 0 or y%400 == 0)
# end def



def daysInMonth(y,m):
    if (m == 4 or m == 6 or m == 9 or m == 11):
        return 30
    # end if
    if (m == 2):
        if (isLeapYear(y)):
            return 29
        else:
            return 28
        # end if
    # end if
    return 31
# end def

def incrementDate(year,month,day):
    day += 1
    dim = daysInMonth(year,month)
    if (day > dim):
        day = 1
        month+=1 
        if (month > 12):
            month = 1
            year += 1 
        # end if
    # end if
    return year, month, day
# end def


# return the number of days in that month
# (year, month, days in month)
def incrementMonth(year,month):
    dim = daysInMonth(year,month)
    month+=1 
    if (month > 12):
        month = 1
        year += 1 
    # end if
    return year, month, dim
# end def




def SolveBySingleDay():
    year = 1900
    month = 1
    day = 1
    nday = 1   # sunday = 0
    dow = nday%7
    nSundaysOnFirstOfMonth = 0
    res_lst = []
    while 1:
        dow = nday%7
        if (year >= 1901 and day==1 and dow == 0):
            print year, month, day, dow
            res_lst.append( (year, month, day) )
            nSundaysOnFirstOfMonth += 1
        # end if

        year, month, day = incrementDate(year,month,day)
        nday +=1
        if (year > 2000):
            break
        # end if        
    #end for
    print nSundaysOnFirstOfMonth
    return res_lst
# end def


def SolveByMonth():
    year = 1900
    month = 1
    day = 1
    nday = 1   # sunday = 0
    dow = nday%7    
    nSundaysOnFirstOfMonth = 0
    res_lst = []

    while 1:
        dow = nday%7
        if (year >= 1901 and day==1 and dow == 0):
            nSundaysOnFirstOfMonth += 1
            res_lst.append( (year, month, day) )
            print year, month, day, dow
        # end if


        year, month, daysInMonth = incrementMonth(year,month)
        nday += daysInMonth

        if (year > 2000):
            break
        # end if
        

    #end for
    print nSundaysOnFirstOfMonth
    return res_lst
# end def


#print isLeapYear(1),isLeapYear(200),isLeapYear(400),isLeapYear(2000),
lst0 = SolveBySingleDay()
lst1 = SolveByMonth()



from datetime import * 

# check for correctness

print lst0 == lst1

# first check all our dates are legitimate 
for d in lst1:
    dt = datetime(d[0], d[1], d[2])
    print d, dt.weekday() == 6  # note: sunday == 6 in the datetime module
# end for

# now check that we included all dates
numsun = 0
for year in range(1901,2001):
    for month in range(1,13):
        dt = datetime(year, month, 1)
        if (dt.weekday() == 6):
            numsun += 1
        # end if
    # end for
# end for
print numsun
