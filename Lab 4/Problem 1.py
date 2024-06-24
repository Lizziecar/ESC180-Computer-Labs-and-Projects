def count_evens(L):
    s = 0
    for num in L:
        if num % 2 == 0:
            s += 1

    return s

if __name__ == "__main__":
    K = [1,2,3,4,5,6,7,8,9,10]
    print(count_evens(K))