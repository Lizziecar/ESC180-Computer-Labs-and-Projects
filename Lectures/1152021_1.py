#Bozosort
#1, 5, 2, 10, 2

#randomly swap pairs until list gets sorted

def is_sorted_nondecreasing(L):
    '''Return True if L is sorted in non-decreasing order'''
    #return L == sorted(L)
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            return False
    return True

import random

def bozosort(L):
    while not is_sorted_nondecreasing(L):
        i, j = int(len(L)*random.random()),  int(len(L)*random.random())
        L[i], L[j] = L[j], L[i]

#time complexity: O(n!)