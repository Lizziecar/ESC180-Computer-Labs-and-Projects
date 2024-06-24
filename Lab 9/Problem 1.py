def top10(L):
    top10 = [0] * 10

    for i in L:
        print(top10)
        for j in range(len(top10)):
            if i >= top10[j]:
                for k in range(len(top10)-1, j, -1): #move list down over by 1
                    top10[k] = top10[k-1]
                top10[j] = i #replace top number
                i = 0 #prevent replacing all the numbers

    return top10




if __name__ == "__main__":
    filename = "text.txt"
    f = open(filename, encoding="latin-1").read().split()

    word_counts = {}
    for i in range(len(f)):
        in_sequence = False
        for w in word_counts:
            if f[i] == w:
                in_sequence = True
        if in_sequence == True:
            word_counts[f[i]] += 1
        else:
            word_counts[f[i]] = 1

    print(word_counts)
    word_counts = {v: k for k, v in word_counts.items()}
    print(word_counts)






