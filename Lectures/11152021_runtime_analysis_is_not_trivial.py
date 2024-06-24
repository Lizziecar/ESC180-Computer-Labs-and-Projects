# Pythagiran Triple
# (a, b, c), such that a^2 + b^2 = c^2
# For example: 3, 4, 5 is a Pythorean triple

# Want to write a function that searches for triples such that
# a^p + b^p = c^p


def fermat(p):
    n = 0
    while True:

        for i in range(1,n):
            for j in range(1,n):
                for k in range(1,n):
                    if i**p + j**p == k**p:
                        return i, j, k

        n += 1

# Fermat's Last Theorem: a^p + b^p = c^p has no integer solutions for p >= 3