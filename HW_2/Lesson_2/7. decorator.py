import time
from datetime import datetime


def time_logger(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} execution time is {(datetime.now() - start).seconds} sec.')
        return result
    return wrapper


@time_logger
def make_list(num):
    my_list = [i for i in range(num)]
    return my_list


@time_logger
def make_list_long(num):
    my_list = [i for i in range(num)]
    time.sleep(3)
    return my_list


# print(time_logger(make_list_long)(10))

print(make_list(10))
print(make_list_long(10))
