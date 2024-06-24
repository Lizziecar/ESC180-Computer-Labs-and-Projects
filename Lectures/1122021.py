##
#Selection sort:

#helper function
def loc_max(L,end):
    '''return local max from 0 to end'''
    cur_max = L[0]
    cur_max_location = 0
    for i in range(1, end + 1): #variable component, runs n times
        if L[i] > cur_max:
            cur_max = L[i]
            cur_max_location = i
    return cur_max_location

#runtime: c1 + c2*n

#selection sort
def selection_sort(L):
    for i in range(len(L)-1): #varialbe amount of times, not constant times n
        #get local max
        max_i = loc_max(L,len(L) - 1 - i)
        #swap the largest element with last spot
        L[max_i],L[len(L) - 1 - i] = L[len(L) - 1 - i],L[max_i]

#runtime: c3 + c1 + c2*(len(L) - 1 - o)
#         c3 + c1 + c2*(len(L) - 1 - 1)
#         ...
#         c3 + c1 + c2 * 1

#Total:
# n = len(L)
# c3 = (n-1)
# c1 = (n-1)
# c2 = (1 + 2 + 3 +... n-1) = n(n+1)/2
# (n-1)(c1+c3)(c2*n(n+1)/2)
# when n is large, n^2 dominates, therefore runtime is O(n^2)

#fast way: two for loops based on length, therefore its n^2

##
#Bubble sort:

def bubble_sort(L):
    for i in range(len(L) - 1):
        swapped = False
        for j in range(len(L) -1 - i):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                swapped = True
        #if there were no swaps, then the list is already sorted
        if not swapped:
            break

#runtime:
#best case: requires no sorts, went through it n times and finished
#worst case: c0 + c1*(n-1 + n-2 + n-3 ... + 1) = c0 + c1*n(n+1)/2 = O(n^2)
#basically proportional to the other one



##
if __name__ == "__main__":
    L = [20,30,43,2,34,67,5,43,2]
    print(L)
    bubble_sort(L)
    print(L)