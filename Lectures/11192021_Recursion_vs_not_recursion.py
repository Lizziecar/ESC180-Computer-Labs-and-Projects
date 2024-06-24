def fact_while(n):
    cur_prod = 1
    i = 1
    while i != n+1:
        cur_prod *= i
        i += 1

    return cur_prod


def fact_iter(n, cur_prod = 1, i = 1): #creates default values
    if i == n+1:
        return cur_prod
    return fact_iter(n,cur_prod * i, i + 1)

def fact(n): #harder to turn into while loop because all the calculations happen at the very end
    if n <= 1:
        return 1
    return n*fact(n-1)