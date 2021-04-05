import re
from collections import namedtuple
from pathlib import Path
from typing import Iterable

from pip._vendor.resolvelib.resolvers import Result


def main():
    pass


if __name__ == "__main__":
    main()


def open_and_read_a_file(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def is_line_valid(line: str) -> bool:
    return len(line.split()) == 5


def is_date_valid(line: str) -> bool:
    return bool(re.search(r"\d{4}-\d{2}-\d{2}", line))


def check_data(line: str, validators: Iterable[Result]) -> str:
    for validator in validators:
        if not validator.result:
            writeAFailureToFile(line)
    return Path("testdata/failures.txt").absolute()


def hw1():
    file = open_and_read_a_file("testdata/data.txt")
    all_lines_from_the_file = file.split("\n", -1)
    for line in all_lines_from_the_file:
        Result = namedtuple('Result', 'result validator_name')
        check_data(line, (
            (Result(is_date_valid(line), is_date_valid.__name__)),
            (Result(is_line_valid(line), is_line_valid.__name__))))


def writeAFailureToFile(content: str):
    with open("testdata/failures.txt", "a") as myfile:
        myfile.write(content)


hw1()
