def euclids_gcd(numerator, denominator):
    numA = numerator
    numB = denominator
    while numA % numB != 0:
        numA, numB = numB, numA % numB

    return str(int(numerator/numB)) + "/" + str(int(denominator/numB))

if __name__ == "__main__":
    print(euclids_gcd(3,6))
    print(euclids_gcd(8,4))
    print(euclids_gcd(16,12))