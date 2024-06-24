def sum_list_3(L,start,end):
    '''Return sum(L[start:end-1])'''

    if start == end:
        return L[start]

    return L[start]+ sum_list_3(L,start + 1,end)

def sum_list_4(L):
    if len(L) == 0:
        return 0

    return sum_list_3(L, 0, len(L)-1)

#runtime is O(n) befcause list_3 does n calls


def sum_list2(L):
    if len(L) == 0:
        return 0
    if len(L) == 1:
        return L[0]
    mid = len(L)//2
    return sum_list2(L[:mid]) + sum_list2(L[mid:])

