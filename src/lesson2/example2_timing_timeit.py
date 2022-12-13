def test1():
    """Write the code you want to test here. For example:"""
    list1 = [4, 5, 7, 2, 5]
    list1.sort()

def test2():
    """Write the code you want to test here. For example:"""
    list1 = [4, 5, 7, 2, 5]
    list2 = sorted(list1)


if __name__ == '__main__':

    #Time testing using timeit module
    import timeit
    print(timeit.timeit("test2()", setup="from __main__ import test2"))

    print(timeit.timeit("test1()", setup="from __main__ import test1"))
