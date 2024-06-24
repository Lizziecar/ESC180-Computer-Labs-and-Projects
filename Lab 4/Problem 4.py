def simplify_fraction(n, m):
    if n < m:
        for num in range(n, 0, -1):
            if n % num == 0 and m % num == 0:
                return str(int(n/num)) + "/" + str(int(m/num))
    else:
        for num in range(m, 0, -1):
            if n % num == 0 and m % num == 0:
                return str(int(n/num)) + "/" + str(int(m/num))


if __name__ == "__main__":
    print(simplify_fraction(3,6))
    print(simplify_fraction(20,10))
    print(simplify_fraction(45,13))
    print(simplify_fraction(1000000000000000000000,2))