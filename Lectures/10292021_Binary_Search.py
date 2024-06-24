#sample code

def binary_search(L, e):
    low = 0 #1
    high = len(L) - 1 #3

    while high - low >= 2: #3
        mid = (low + high)//2 #3
        if L[mid] < e: #3
            low = mid + 1 #2
        elif L[mid] > e: #3
            high = mid - 1 #2
        else:
            return mid #1

    if L[low] == e: #3
        return low #1
    elif L[high] == e: #3
        return high
    else:
        return None #1

'''Overall runtime in the worst case:
4 (first part) + 7 (last part) + k*11 (while loop)
K is the amount of times the while loop iterates

approximately = 11 + 11 * log2(n) = 11 + 11 * log(n) * log(n)/log10
so we just say log(n)

High - low: len(L) + 2^k-
            (len(L) -1) / 2
            (len(L) - 1) / 4
            ...
2^k-1 = n - 1
k - 1 = log2(n-1)
kx = log2(n)

'''
##
if __name__ == "__main__":
    L = [0]*100000000
    L[499] = 3

    print(binary_search(L , 3))
