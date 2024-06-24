# Recursion: functions that call themselves

#n! = 1*2*3*4...*n
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

# Recursion functions f:
# 1. Base case (an input where you know the output
# 2. Recursive step (the answer in terms of the function f)

def fact_no_base_case(n):
    return n * fact_no_base_case(n-1)