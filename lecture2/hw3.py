from typing import Any, List


def main():
    pass


if __name__ == "__main__":
    main()


def combinations(*args: List[Any]) -> List[List]:
    my_list = []
    for indexI in range(len(args) - 1):
        for i in args[indexI]:
            for indexK in range(indexI, len(args) - 1):
                for k in args[indexK + 1]:
                    my_list.append([i, k])
    return my_list


combinations([1, 2], [3], [4, 5], [6, 7], [8, 9])
