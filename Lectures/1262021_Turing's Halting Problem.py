#Turing's Halting Problem and Goedel Incompleteness Theorem

a = '''def f():
    while True:
        pass'''

'''def g():
    n=3
    while True:
        if n % 2 == 0 and is_prime(n):
            return
        n += 1'''

''' def fermat(p):
        n = 1
        while True:
            for i in range(1, n):
                for j in range(1, n):
                    if i**p + j**p == k**p:
                        return i, j, k
            n += 1'''

def halt(f, x):
    '''Return True if f(x) halts, and false if f(x) produces an infinite loop'''


def confused(f):
    if halt(f, f):
        while True:
            pass
    else:
        return False

# confused(confused) -> halts -> halt(confusedm,confused) must be False
# => confused(confused) produces an infinite loop => CONTRADICTION

#confused(confused) doesn't halt => halt(confused,confused) must be true
#=> confused(confused) halts


def f():
    return None

import inspect
inspect.getsource(f)