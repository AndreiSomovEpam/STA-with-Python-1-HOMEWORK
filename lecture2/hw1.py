import re
from collections import namedtuple
from pathlib import Path
from typing import Iterable

from pip._vendor.resolvelib.resolvers import Result


def open_and_read_a_file(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def validate_line(line: str) -> bool:
    return len(line.split()) == 5


def validate_date(line: str) -> bool:
    return bool(re.search(r"\d{4}-\d{2}-\d{2}", line))


def check_data(line: str, validators: Iterable[Result]) -> str:
    for validator in validators:
        if not validator.result:
            write_failure_to_file(line)
    return Path("testdata/failures.txt").absolute()


def hw1():
    file = open_and_read_a_file("testdata/data.txt")
    all_lines_from_the_file = file.split("\n", -1)
    for line in all_lines_from_the_file:
        Result = namedtuple('Result', 'result validator_name')
        check_data(line, (
            (Result(validate_date(line), validate_date.__name__)),
            (Result(validate_line(line), validate_line.__name__))))


def write_failure_to_file(content: str):
    with open("testdata/failures.txt", "a") as myfile:
        myfile.write(content)


hw1()
