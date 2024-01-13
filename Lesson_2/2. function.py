from typing import Callable


def calc_sum(a: int, b: int) -> int:
    return a + b


def calc_sub(a: int, b: int) -> int:
    """This function used for subtraction"""
    return a - b

def print_hello():
    print("Hello")

# print_hello()

# print(type(calc_sub))
# print(calc_sub.__doc__)
# print(calc_sub.__name__)

#a = calc_sub
#print(a(10, 5))

my_list = [calc_sub, calc_sum]

#for func in my_list:
#    print(func(15, 10))


#def some_func(func: Callable, a: int, b: int) -> any:
#    print(func(a, b))


#some_func(calc_sum, 5, 10)
#some_func(calc_sub, 10, 5)
