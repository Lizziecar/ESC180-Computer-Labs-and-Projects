# L is sorted
# [1, 5, 100, 102, 105, 200, 250, 500, 520, 500]
#Find 520
#Seach algorithms I think

##
#binary search

def find_i_binary(L, e):
    #currently looking at L[low] ... L[high]
    low = 0
    high = len(L) - 1
    while(high - low >= 2):
        mid = (low + high) // 2
        if L[mid] > e:
            high = mid-1
        elif L[mid < e]:
            low = mid + 1
        else:
            return mid

    if L[low] == e:
        return low
    elif L[high] == e:
        return high
    else:
        return None

