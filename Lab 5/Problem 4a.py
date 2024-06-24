def print_matrix_dim(M):
    print(len(M), "x", len(M[0]))

if __name__ == "__main__":
    M = [[1,2],
        [3,4],
        [5,6]]

    print_matrix_dim(M)