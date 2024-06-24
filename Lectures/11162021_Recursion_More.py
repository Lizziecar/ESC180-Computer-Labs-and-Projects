def print_list(L):
    '''Print the list L'''

    #base case
    if len(L) == 1:
        print(L[0])
        return

    print(L[0])
    print_list(L[1:])