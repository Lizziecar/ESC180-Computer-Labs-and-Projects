# Recurusion with caching

def fib(n): #O(fib)
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

'''
........................................
        fib(n-3)      fib(n-2)
    \ /           \  /
    fib(n-2)        fib(n-1)
       \              /
            fib(n)

Calls(n) = 1 + Calls(n-1) + Calls(n-2) ~= fib(n)
'''

def fib(n,cache = {1: 1., 2:1.}):
    if n in cache:
        return cache[n]

    if n <= 2:
        return 1
    # if n-1 in cache:
    #    fibn1 = cache[n-1]
    #else:
    #    fibn1 = fib(n-1, cache)
    #    cache[n-1] = fibn1
    #if n-2 in cache:
    #    fibn2 = cache[n-2]
    #else:
        fibn2 = fib(n-2, cache)
        cache[n-2] = fibn2

    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


'''
................................
   fib(n-4)   fib(n-3)          fib(n-2)
    \        /           \       /
    fib(n-2)        fib(n-1)
       \              /
            fib(n)
            '''
#Need to really compute fib(1), fib(2), ... fib(n) once
#Other intermediate computations take just two calls
# Complexity: O(n)