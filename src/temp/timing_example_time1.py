def test():
    """Write the code you want to test here. For example:"""
    L = [i for i in range(100)]


if __name__ == '__main__':
    #Time testing using time module
    import time

    beginning = time.time()
    for i in range(0,1000000):      # Calls tested function million times
        test()

    end = time.time()
    print("time: ", end-beginning, "s")