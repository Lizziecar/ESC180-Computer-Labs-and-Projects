import numpy as np


# Printing matrices using NumPy:

# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
print(M)

def print_matrix(M_lol):
    N = np.array(M_lol)
    print(N)

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    #all numbers were zero
    return len(row)

def get_row_to_swap(M, start_i):
    #only check rows greater than start_i
    index_row_to_be_swapped = start_i
    current_lead_ind = len(M[0])
    for i in range(start_i,len(M)):
        if get_lead_ind(M[i]) < current_lead_ind:
            current_lead_ind = get_lead_ind(M[i])
            index_row_to_be_swapped = i

    return index_row_to_be_swapped

def add_rows_coefs(r1, c1, r2, c2):
    new_list = [0] * len(r1)
    for i in range(len(new_list)):
        new_list[i] = c1*r1[i] + c2*r2[i]

    return new_list

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub + 1, len(M)):
        #find c
        c = -(M[i][best_lead_ind] / M[row_to_sub][best_lead_ind])
        M[i] = add_rows_coefs(M[row_to_sub], c, M[i], 1)

def eliminateBackward(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub - 1, -1, -1):
        #find c
        c = -(M[i][best_lead_ind] / M[row_to_sub][best_lead_ind])
        M[i] = add_rows_coefs(M[row_to_sub], c, M[i], 1)

def divide_rows_coefficient(M):
    for i in range(len(M)):
        leading_coefficient = M[i][get_lead_ind(M[i])]
        for j in range(len(M[i])):
            M[i][j] /= leading_coefficient

def forward_step(M):
    print("Now performing forward step")

    #current Matrix
    print("The matrix is currently:")
    print_matrix(M)

    for i in range(len(M)):
        #check swap
        row_to_swap = get_row_to_swap(M,i)
        print("Now looking at row: ", i)

        #swap rows
        M[i],M[row_to_swap] = M[row_to_swap],M[i]
        column = get_lead_ind(M[i])
        print("Swapping rows ", i, "and ", row_to_swap, "so that entry ", column,"in current row is non-zero")

        #current Matrix
        print("The matrix is currently:")
        print_matrix(M)

        #elimiate
        print("Adding row ", i, " to rows below it to eliminate coefficients in column ", column)
        eliminate(M, i, column)

        #current Matrix
        print("The matrix is currently:")
        print_matrix(M)

        print("================================================================================")

    #final statements
    print("Done with the forward step")
    #current Matrix
    print("The matrix is currently:")
    print_matrix(M)

def backward_step(M):
    print("Now performing the backward step")
    for i in range(len(M)-1, -1, -1):
        column = get_lead_ind(M[i])

        #elimiate
        print("Adding row ", i, " to rows below it to eliminate coefficients in column ", column)
        eliminateBackward(M, i, column)

        #current Matrix
        print("The matrix is currently:")
        print_matrix(M)

    #divide by coefficients
    print("Now dividing each row by the leading coefficient")
    divide_rows_coefficient(M)

    #current Matrix
    print("The matrix is currently:")
    print_matrix(M)

def solve(M,b):
    #build augmented Matrix
    W = M
    for i in range(len(W)):
        W[i].append(b[i])

    #Gaussian elimination
    forward_step(W)
    backward_step(W)

    #solve for x
    x = [0]*len(W)
    for i in range(len(x)):
        x[i] = W[i][len(W[i])-1] #last element of row

    return x

if __name__ == "__main__":
    #Test
    Mnp = np.array([[1,-2,3],[3,10,1],[1,5,3]])
    xnp = np.array([2,13,-11])
    bnp = np.matmul(Mnp,xnp)

    M = Mnp.tolist()
    x = xnp.tolist()
    b = bnp.tolist()

    GEx = solve(M,b)
    print(GEx)
    if GEx == x:
        print("Success")




'''#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
b = np.matmul(M,x)

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

# To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist()

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]'''