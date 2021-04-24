from collections.abc import Callable


def func1(a, b):
    return (a ** b) ** 2


def cache(func: Callable) -> Callable:
    prev_args = None
    prev_result = None

    def inner(*args):
        nonlocal prev_args, prev_result
        if prev_args == args:
            return prev_result
        prev_args = args
        prev_result = func(*args)
        return prev_result
    return inner


cache_func = cache(func1)

print(cache_func(2, 2))
