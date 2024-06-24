def list_to_str(lis):
    list_as_string = "'["
    for num in range(len(lis)):
        if num == 0:
            list_as_string += str(lis[num])
        else:
            list_as_string += ", " + str(lis[num])

    list_as_string += "]'"
    return list_as_string


if __name__ == "__main__":
    K = [1,2,3]
    print(list_to_str(K))
    M = [4,5,6,7]
    print(list_to_str(M))