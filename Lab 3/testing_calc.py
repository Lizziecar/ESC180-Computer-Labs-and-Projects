import lab02

if __name__ == '__main__':
    lab02.initialize()

    #Test 1
    lab02.add(42)
    if lab02.get_current_value() == 42:
      print("Test 1 passed")
    else:
      print("Test 1 failed")

    #Test 2
    lab02.subtract(2)
    if lab02.get_current_value() == 40:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    #Test 3
    lab02.multiply(2)
    if lab02.get_current_value() == 80:
        print("Test 3 passed")
    else:
        print("Test 3 failed")

    #Test 4
    lab02.divide(40)
    if lab02.get_current_value() == 2:
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    #Test 5
    lab02.store()
    lab02.add(50)
    lab02.recall()
    if lab02.get_current_value() == 2:
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    #Test 6
    lab02.add(5)
    lab02.undo()
    if lab02.get_current_value() == 2:
        print("Test 6 passed")
    else:
        print("Test 6 failed")