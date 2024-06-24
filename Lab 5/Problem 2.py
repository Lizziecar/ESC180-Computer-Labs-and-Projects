def match_pattern(list1, list2):
    if len(list1) < len(list2): #wrong sizes
        return False

    for i in range(len(list2)):
        if list1[i] == list2[0]:
            for j in range(len(list2)):
                if list1[i + j] != list2[j]:
                    return False
                else:
                    return True

    #the first number of list2 DNE in list1
    return False

if __name__ == "__main__":
    list1 = [4, 10, 2, 3, 50, 100]
    list2 = [2, 3, 50]

    print(match_pattern(list1,list2))

    list1 = [4,3]
    list2 = [6,5,6]

    print(match_pattern(list1,list2))