def repeats(list0):
    for i in range(len(list0)-1):
        if list0[i] == list0[i+1]:
            return True

    return False

if __name__ == "__main__":
    list0 = [1,2,3,3,4]
    print(repeats(list0))

    list1 = [1,2,3]
    print(repeats(list1))