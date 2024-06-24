import math

#From Lab 3

def pi_estimate(n):
    total = 0
    for i in range(0, n+1):
        total += ((-1)**i)/(2*i + 1)

    #should return π/4
    return total*4

def terms_for_pi(significant_digits):
    significant_digits -= 1
    num = 0
    pi_estimate_value = pi_estimate(num)
    while ((int(pi_estimate_value*(10**significant_digits))) != (int(math.pi*(10**significant_digits)))):
        pi_estimate_value = pi_estimate(num)
        num += 1

    return num

def terms_for_pi2(significant_digits):
    significant_digits -= 1
    num = 0
    total = 0
    while True:
        total += ((-1)**num)/(2*num + 1)

        #should return π/4
        pi_estimate = total*4
        if (int(pi_estimate*(10**significant_digits))) == (int(math.pi*(10**significant_digits))):
            break
        else:
            num += 1

    return num

if __name__ == "__main__":

    '''print("1 sig-fig: ", terms_for_pi(1))
    print("2 sig-fig: ", terms_for_pi(2))
    print("3 sig-fig: ", terms_for_pi(3))
    print("4 sig-fig: ", terms_for_pi(4))
    #5 sig figs takes a bit'''

    print(terms_for_pi2(5))