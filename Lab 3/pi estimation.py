def pi_estimate(n):
    total = 0
    for i in range(0, n+1):
        total += ((-1)**i)/(2*i + 1)

    #should return π/4
    return total*4

if __name__ == "__main__":
    print(pi_estimate(1000)) #test with an n value of 1000