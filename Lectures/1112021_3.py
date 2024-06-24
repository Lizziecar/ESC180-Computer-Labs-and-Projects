import random
import time

def get_seq_ab(length):
    s = ""
    for i in range(length):
        if random.random() > .5:
            s += "a"
        else:
            s += "b"
    return s

def f1(x):
    return 2*x

def f2(x):
    return 10*x

def applyit(f):



def timeit(func, arg1, arg2):
    '''Return the estimate of the runtime, in seconds, of func(arg1, arg2),
    by running the command several times and averaging the results'''
    N = 50
    t0 = time.time()
    for i in range(N):
        func(arg1, arg2)
    t1 = time.time()
    return (t1-t0)/N