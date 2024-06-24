#Problem 4

def zigzag2(L):
    n = len(L)
    if len(L) == 0:
        print('')
    elif len(L) == 1:
        print(L[n-1]//2, end = "")
    else:
        print(L[0]//2, L[0]//2, end = " ")
        zigzag2(L[1:-1])

if __name__ == "__main__":
    L = (2,4,6,8,10,12,14,16,18)
    zigzag2(L)

