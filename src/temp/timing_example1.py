def test():
    """Write the code you want to test here. For example:"""
    L = [i for i in range(100)]

if __name__ == '__main__':

    #Time testing using timeit module
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))

    #Time testing using time module
    import time

    beginning = time.time()
    for i in range(0,1000000):
        test()
    # testattava koodi
    end = time.time()
    print("time: ", end-beginning, "s")



    list1 = [4, 5, 7, 2, 5]
    list2 = list1.sort()
    print(lista2)
c