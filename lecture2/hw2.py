from collections import Counter
from typing import List, Tuple


def main():
    pass


if __name__ == "__main__":
    main()


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    return Counter(inp).most_common()[0][0], Counter(inp).most_common()[-1][0]


major_and_minor_elem([2, 2, 2, 3, 3])
