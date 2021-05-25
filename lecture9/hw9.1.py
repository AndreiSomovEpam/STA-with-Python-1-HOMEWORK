"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
Add tests for this function.
"""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    list = []
    for path in file_list:
        with open(path) as file:
            list.extend(row.strip() for row in file.readlines())
    list.sort()
    return iter(list)


def test_merge_sorted_files():
    assert(isinstance(merge_sorted_files(["file1.txt", "file2.txt"]), Iterator))