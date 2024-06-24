#Mergesort
#split list in half and sort each section seperatly
#then combine together in the end

def merge(L1,L2):
    merged = []
    i,j = 0,0

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1

    merged.extend(L1[i:])
    merged.extend(L2[j:])

    return merged

def merge_sort(L):
    if len(L) <= 1:
        return L[:]
    else:
        mid = len(L) // 2
        return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))
