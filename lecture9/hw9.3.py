"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import fnmatch
import os
import tokenize
from io import StringIO
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    list = []
    for path in fnmatch.filter(os.listdir(dir_path), "*." + file_extension):
        p = str(dir_path) + "/" + path
        with open(p) as f:
            if tokenizer:
                s = tokenizer.generate_tokens(StringIO(f.read()).readline)
                return sum(1 for _ in s)
            list.extend(f.readlines())
    return len(list)


print(universal_file_counter(Path("test_dir"), "txt", tokenize))
