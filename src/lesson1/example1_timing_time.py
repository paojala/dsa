def test1():
    """Write the code you want to test here. For example:"""
    list1 = [4, 5, 7, 2, 5]
    list1.sort()

def test2():
    """Write the code you want to test here. For example:"""
    list1 = [4, 5, 7, 2, 5]
    list1 = sorted(list1)


if __name__ == '__main__':
    #Time testing using time module
    import time

    beginning = time.time()
    for i in range(0,1000000):      # Calls tested function million times
        test1()

    end = time.time()
    print("time: ", end-beginning, "s")


    beginning = time.time()
    for i in range(0,1000000):      # Calls tested function million times
        test2()

    end = time.time()
    print("time: ", end-beginning, "s")