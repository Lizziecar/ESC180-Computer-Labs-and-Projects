def sum_of_cubes(n):
    total = 0
    for i in range(1, n+1):
        total += i**3

    return total

def sum_of_cubes_formula(n):
    return ((n**2)*(n+1)**2)/4

def check_sum(n):
    if sum_of_cubes(n) == sum_of_cubes_formula(n):
        return True
    else:
        return False

def check_sums_up_to_n(n):
    for i in range(1, n+1):
        if check_sum(i) == False:
            return False


    return True

if __name__ == "__main__":

    #Testing the functions
    x = 5
    print("Sum of Cubes without Formula: ", sum_of_cubes(x))
    print("Sum of Cubes with Formula: ", sum_of_cubes_formula(x))
    print() #newline

    #Trying check_sum()
    print("Checking at n = 5: ", check_sum(5))
    print("Checking at n = 40: ", check_sum(40))
    print() #newline

    #Trying check_sums_up_to_n()
    print("Testing all the values up until 40: ", check_sums_up_to_n(40))

