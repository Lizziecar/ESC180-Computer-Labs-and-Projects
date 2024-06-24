A = {(0,0): 1, (0,1): 2, (0,2): 3, (1,0): 4, (1,1): 5, (1,2): 6}
B= {(0,0): 6, (0,1): 5, (0,2): 4, (1,0): 3, (1,1): 2, (1,2): 1}
dim = (2,3)

sum_matrix = [[0 for i in range(3)] for i in range(2)]
for i in range(dim[0] - 1):
    for j in range(dim[1] - 1):
        sum_matrix[i][j] = A[(i,j)] + B[(i,j)]

print(sum_matrix)