"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
# >>> with supressor(IndexError):
# ...    [][2]
"""
from contextlib import contextmanager

from lecture9.Supressor import Supressor

with Supressor(IndexError):
    my_list = [0]
    my_list[1]


@contextmanager
def supressor(exception):
    try:
        yield
    except exception:
        print("IndexError has been handled")
        pass


with supressor(IndexError):
    my_list = [0]
    my_list[1]
