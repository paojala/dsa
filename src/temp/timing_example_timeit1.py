# https://docs.python.org/3/library/timeit.html

def test():
    """Write the code you want to test here. For example:"""
    L = [i for i in range(100)]

if __name__ == '__main__':

    #Time testing using timeit module
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))