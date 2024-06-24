#Problem 2

def interleave(L1, L2):
    inter = []
    if L1 == [] and L2 == []:
        return inter
    elif L1 == [] and L2 != []:
        return L2

    elif L1 != [] and L2 == []:
        return L1
    else:
        if len(L1) >= len(L2):
            inter.append(L1[0])
            inter = inter + interleave(L1[1:], L2)
        else:
            inter.append(L2[0])
            inter = inter + interleave(L1, L2[1:])

    return inter

if __name__ == "__main__":
    L1 = [1,2,3,4,5]
    L2 = [5,4,3,2,1]

    print(interleave(L1,L2))