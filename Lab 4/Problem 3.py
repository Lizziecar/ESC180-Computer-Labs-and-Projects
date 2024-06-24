def list_are_the_same(list1, list2):
    if len(list1) != len(list2): #check to see if the list lengths are equal. If they are not then we know
                                 # that they won't be equal
        return False

    for num in range(len(list1)): #I can do this because I know the lengths are equal
        if list1[num] != list2[num]:
            return False

    return True

if __name__ == "__main__":
    K = [1,2,3]
    M = [5,4,3]
    J = [1,2,3]

    print(list_are_the_same(K,M))
    print(list_are_the_same(K,J))