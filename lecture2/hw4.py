from collections.abc import Callable


def main():
    pass


if __name__ == "__main__":
    main()


def func1(a, b):
    return (a ** b) ** 2


def cache(func: Callable) -> Callable:
    print("some caching logic here")
    return func


cache_func = cache(func1)


print(cache_func(2, 2))
