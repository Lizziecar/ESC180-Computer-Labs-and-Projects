#exam prep

#Recursive function with complexity O(n^2)*log(n)

import numpy

def counter(k):
    if k == 0:
        return 1
    else:
        return counter(k-1.0)

def f(n):
    return counter(n**2 * numpy.log(n))