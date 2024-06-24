# How efficient is the function f?
# For an input of size n, in the worst case, what is the runtime proportional to?

def f(L):
    if L[0] == 5:
        return

    #len(L) * len(L)//2 times
    for i in range(len(L)):
        for j in range(len(L)//2):
            print("hi") #const amt of time

# Total runtime: const1 + const*len(L)*len(L)//2
# The runtime is proportional to n^2, where n = len(L)    (for large n)
# Asymptotic worst-case runtime complexity is: O(n^2)