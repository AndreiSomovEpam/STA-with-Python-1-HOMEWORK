import itertools
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    my_list = []
    combinations = itertools.combinations(args, 2)
    for combination in combinations:
        for one in combination[0]:
            for two in combination[1]:
                my_list.append([one, two])

    return my_list


combinations([1, 2], [3], [4, 5, 6], [7], [8, 9])
