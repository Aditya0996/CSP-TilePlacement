from unittest import TestCase
from unittest.mock import patch

from main import getResult


class Test(TestCase):
    def test_get_result1(self):
        file = "test/test1.txt"
        result = getResult(file)
        self.assertTrue(result != False)

    def test_get_result2(self):
        file = "test/test2.txt"
        result = getResult(file)
        self.assertTrue(result != False)

    def test_get_result3(self):
        file = "test/test3.txt"
        result = getResult(file)
        self.assertTrue(result != False)

    def test_get_result4(self):
        file = "test/test4.txt"
        result = getResult(file)
        self.assertTrue(result != False)

    def test_get_result5(self):
        file = "test/test5.txt"
        result = getResult(file)
        self.assertTrue(result != False)

    def test_get_result6(self):
        file = "test/test6.txt"
        result = getResult(file)
        self.assertTrue(result != False)

    def test_get_result7(self):
        file = "test/test7.txt"
        result = getResult(file)
        self.assertTrue(result != False)

    def test_get_result8(self):
        file = "test/test8.txt"
        result = getResult(file)
        self.assertTrue(result != False)

    def test_get_result9(self):
        file = "test/test9.txt"
        result = getResult(file)
        self.assertTrue(result != False)

    def test_get_result10(self):
        file = "test/test10.txt"
        result = getResult(file)
        self.assertTrue(result != False)
