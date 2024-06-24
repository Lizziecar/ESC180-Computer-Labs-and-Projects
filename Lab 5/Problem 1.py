def list1_starts_with_list2(list1, list2):
    if len(list1) < len(list2):
        return False
    for i in range(len(list2)):
        if list1[i] != list2[i]:
            return False

    return True


if __name__ == "__main__":
    L1 = [1, 2, 3, 4]
    L2 = [1,2,3]
    print(list1_starts_with_list2(L1, L2))

#How do you do without loops?