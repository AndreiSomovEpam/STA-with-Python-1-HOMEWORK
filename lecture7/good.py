"""
Ready implementation of bad.py
See the task in good.py
"""
import logging
from collections import defaultdict
from typing import Dict, List

from lecture7.CustomIterator import CustomIterator

logging.basicConfig(level=logging.INFO)


def create_country_make_dict() -> Dict[str, List[str]]:
    country_manufacturers: Dict[str, List[str]] = defaultdict()
    iterator = CustomIterator()
    while True:
        try:
            json = next(iterator)
            for manufacturer in json["Results"]:
                country_manufacturers = country_manufacturers | {manufacturer["Country"]: manufacturer["Mfr_Name"]}
        except StopIteration:
            return country_manufacturers


print(create_country_make_dict())