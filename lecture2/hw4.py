from collections.abc import Callable


def func1(a, b):
    return (a ** b) ** 2


def cache(func: Callable) -> Callable:
    def inner(a, b):
        return func(a, b)
    return inner


cache_func = cache(func1)

print(cache_func(2, 2))
