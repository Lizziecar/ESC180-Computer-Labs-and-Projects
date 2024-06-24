#Problem 3

def reverse_rec(L):
    if len(L) == 0:
        return []
    return [L[-1]] + reverse_rec(L[:-1])


if __name__ == "__main__":
    L = (1,2,3,5,6,7,8,9,10,11,12,13,14,15)
    print(reverse_rec(L))