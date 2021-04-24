import itertools
from typing import Any, List


def combinations(*args: List[Any]) -> list[tuple[Any, ...]]:
    my_list = []
    for i in itertools.product(*args):
        my_list.append(i)
    return my_list


print(combinations([1, 2], [3, 4]))