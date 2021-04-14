import unittest
from lecture4.tests.hw1 import func


class DefaultTestCase(unittest.TestCase):

    def test_func(self):
        print("running test")
        assert func(239, 30) == [7, 1, 29]


#pytest DefaultTestCase.py -v --html=report.html --self-contained-html
