#!/usr/bin/python

def n_is_prime(n, primes):
    for p in primes:
        if (n%p==0):
            return False
        # end if
    # end for
    return True
# end def


primes = []

# for a number of value n, we only need to consider the primes which are 
# less than sqrt(n) <- thhis only applies to if it's prime or not
# not if we have enough factors to factor a number
# that would require (assuming it isn't prime) to half-x
#
# HOWEVER: we want to consider if the number is prime itself, 
# we could optimize that away since it implies the number only has 
# two divisors (??? this may not work)
def have_enough_primes(n, primes):
    if (len(primes) == 0):
        return False
    # end if
    if (primes[-1] > n):
        return True
    # end if
    return False
# end def

def generate_more_primes(n, primes):
    if (len(primes) == 0):
        i = 2
    else:
        i = primes[-1] + 1
    # end if
    maxprime = n
    while i <= maxprime:
        if (n_is_prime(i,primes)):
            primes.append(i)
        # end if
        i+=1
    # end while    
# end def

def get_primes_upto(n):
    generate_more_primes(n, primes)
    return primes
# end def

def get_max_pow(n, a):
    # if n = a^i*b, where b is a whole number, returns i
    i = 1
    while n%(a**i)==0:
        i+=1
    # end while
    return i-1
# end def

# ignore 1
def factor(n):
    if (not have_enough_primes(n+1, primes)):
        generate_more_primes(n+1, primes)
    # end if
    if (n == 0):
        return [] # corner case
    # end if
    divisors = []
    number = n
    for i in primes:
        if (number == 1):
            break
        # end if        
        if (number%i == 0):
            exponent = get_max_pow(number,i)
            number = number/i**exponent
            divisors.append((i, exponent))
        # end if
    # end for
    return divisors
# end for

def merge_factor_list(a, b):
    fa = [ f for (f,e) in a ]
    fb = [ f for (f,e) in b ]
    result = []
    while (fa != [] or fb != []):
        if (fa == []):
            result.append(b[0])
            b = b[1:]
            fb = fb[1:]
        elif (fb == []):
            result.append(a[0])
            a = a[1:]
            fa = fa[1:]
        elif (fa[0] < fb[0]):
            result.append(a[0])
            a = a[1:]
            fa = fa[1:]
        elif (fa[0] > fb[0]):
            result.append(b[0])
            b = b[1:]
            fb = fb[1:]
        else:
            result.append( (a[0][0], a[0][1] + b[0][1]) )
            a = a[1:]
            b = b[1:]
            fa = fa[1:]
            fb = fb[1:]
        # end if
    # end while
    return result
# end def

def remove_factor_from_list(factor_list, (factor, exponent)):
    idx = 0
    for (f,e) in factor_list:
        if (f == factor):
            # we break after mutating the list, so no big issue
            res = e - exponent
            if (res == 0):
                del factor_list[idx]
            elif (res < 0): 
                return False
            else:
                factor_list[idx] = (f, res)
            # end 
            return True
        # end if
        idx+=1
    # end for

    return False
# end def


def generate_proper_divisors(n):
    divlist = []
    for i in range(1, n):
        if (n%i == 0):
            divlist.append(i)
        # end if
    # end for
    return divlist
# end def


def increment_factor_count(count, factors):
    nfactors = len(factors)
    count[0]+=1
    for i in range(0,nfactors):
        if (count[i] > factors[i][1]):
            count[i] = 0
            count[i+1] += 1
        # end def
    # end 
# end def


def generate_divisor(count, factors):
    return reduce(lambda x,y: x*y, [ f**p for p,(f,maxp) in zip(count, factors) ])
# end def

def generate_proper_divisors_from_factors(factors):
    pdivs = []

    if (len(factors) == 0):
        return []
    # end if

    ndivs = reduce(lambda x,y:x*y,[ factor[1]+1 for factor in factors ])
    count = [0]*len(factors)
    
    for i in range(0, ndivs-1):
        pdivs.append(generate_divisor(count, factors))
        increment_factor_count(count, factors)
        #print factors[i]
    # end for
    pdivs.sort()
    return pdivs
# end def

def generate_proper_divisors(n):
    factors = factor(n)
    return generate_proper_divisors_from_factors(factors)
# end def
