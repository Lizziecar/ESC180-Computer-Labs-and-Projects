def mult_mat_vect(M, Mdim, v):
    '''Multiply the sparse matrix M of dimension Mdim by the fector v'''
    res = [0] * Mdim[0]
    for coords, entry in M.items():
        res[coords[0]] += entry * v[coords[1]]

    return res

if __name__ == "__main__":
    M = {(0,3): 1, (0,1): 1, (1, 4): 5, (2, 0): 2}
    Mdim = (3, 5)
    v = [1, 2, 3, 4, 5]