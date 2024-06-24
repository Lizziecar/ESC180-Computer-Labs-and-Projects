#Problem 5

def is_balanced(s):
    a = s.find("(")
    b = s.find(")",-1,0)
    print(s)

    if s.find("(") != -1 and s.find(")") != -1:
        return is_balanced(s[a:b])
    if s.find("(") != -1 or s.find(")") != -1:
        return False
    else:
        return True





if __name__ == "__main__":
    s = "(())"
    print(is_balanced(s))

