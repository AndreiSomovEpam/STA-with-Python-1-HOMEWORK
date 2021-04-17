import unittest
from lecture4.tests.hw1 import func


class defaulttestcase(unittest.TestCase):

    def test_func(self):
        print("running test")
        assert func(239, 30) == [7, 1, 29]


    def test_devide_by_zero(self):
        assert func(747, 0) == []


#pytest defaulttestcase.py -v --html=report.html --self-contained-html
