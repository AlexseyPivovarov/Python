def test_time(func):
    def wrapper(*args):
        from time import time
        start = time()
        a = func(*args)
        end = time()
        print("{} time {}".format(func.__name__, round(end - start, 6)))
        return a
    return wrapper
