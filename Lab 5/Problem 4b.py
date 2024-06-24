def mult_M_v(M,v):
    #create
    N = [0] * len(M)

    for i in range(len(M)):
        N[i] = M[i][0]*v[0] + M[i][1]*v[1]

    return N
if __name__ == "__main__":
    M = [[1,2,],
        [3,4],
        [5,6],
        [7,8]]
    v = [1,2]

    print(mult_M_v(M,v))
