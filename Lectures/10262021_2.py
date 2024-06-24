#This will be on the exam

#Analysis of runtime complexity
#How efficient or inefficient a function is

#example
def find_i(L, e):
        '''return the index of the first appearance of
        e in L or none if e is not L'''
        #return L.index(e)

        for i in range(len(L)): #one operation
            if L(i) == e: #two operations
                return i #one operation

        return None #one operations


#worst-case runtime compelxity: the runtime
#in the worst case, for input of size n

# worst case: e is not in L
# 3*n + 1 operatons
#the runtime will be proportional to (3*n + 1)
#the runtime in the worst case, for large n,
#will be proportional to n
# The tight upper bound on the asymptotic runtime
# complexity of find_i is O(n)