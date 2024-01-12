# # Позиционные, обязательные
def positional_args(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")


positional_args(1, 2, "some")


# Именованные (имеющие значения по умолчанию)
def named_args(a, b, c="some"):
    print(f"a = {a}, b = {b}, c = {c}")


named_args(a=5, b=10)
named_args(a=5, b=10)


def func_args(*args):
    for num in args:
        print(num)
    print(f"args = {args}")


func_args(1, 2, 3, 4)

my_list = [1, 2]
my_tuple = (1, 2)


def func_kwargs(**kwargs):
    kwargs.get("a")
    print(f"kwargs = {kwargs}")


func_kwargs(a=1, b=2, some=10, c=76)


# def any_of_any(*args, **kwargs):
#     print(f"args = {args}")
#     print(f"kwargs = {kwargs}")
#
#
# any_of_any(1, 2, 3, 4, test=1, money=2)


# # Распаковка значений при передаче в функцию
# d = {"host": "127.0.0.1", "port": 6435, "topic_name": "smth"}
#
#
# def func_unpack(host: str, port: int, topic_name: str):
#     print(f"Config: host: {host}, port: {port}")
#
#
#
# func_unpack(**d)

