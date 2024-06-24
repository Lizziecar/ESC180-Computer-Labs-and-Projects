#Counting sort/ Bucket Sort


#bucket sort general
'''1 - 100, 101 - 200, 201 - 300, ...
'''

#counting sort, each bueckt is of size 1

#[1,0,0,10,1,100] sort this
'''
0 , 1, ... 10, ..., 100
0   1      10       100
0   1
'''

#sorted (read aleft to right): [0, 0, 1, 1, 10, 100]


def counting_sort(L):
    max_int = max(L) #O(n) or k1*n time

    counts = [0] * (1 + max_int) #O(m) or k2 *m time

    for e in L:
        counts[e] += 1 #O(n) or k3*n time

    sorted_L = []
    for i in range(0, len(counts)): # k4*n + k5*m ebcuase we're extending sorted_L by n elements in total, and the loop itself runs m+1 times
        sorted_L.extend([i] * counts[i])

    L[:] = sorted_L #k6 *n

#Total: (k1 + k3 + k4 + k6)*n + (k2 + k5)*m time
#O(n+m)