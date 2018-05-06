#!/usr/bin/python3
"""Module docstring
Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
        """Class docstring
        unittest for max_integer
        """

        def testForImport(self):
                    self.assertTrue(__import__('6-max_integer').max_integer)
                    def testSimple(self):
                        n_list = [3, 4, 5, 6]
                        self.assertEqual(max_integer(my_list), 6)

                    def testVar(self):
                        i = 69
                        n_list = [1, 5, 3, i]
                        self.assertEqual(max_integer(my_list), i)
                    def testSingle(self):
                        n_list = [7]
                        self.assertEqual(max_integer(my_list), 7)
                    def testNone(self):
                        n_list = []
                        self.assertEqual(max_integer(my_list), None)
                    def testString(self):
                        n_list = ['x-ray', 'zebra', 'moss']
                        self.assertEqual(max_integer(my_list), 'zebra')

                    def testFailSimple(self):
                        n_list = [1, 3, 'X']
                        self.assertRaises(TypeError, max_integer, my_list)

                    def testFalseDict(self):
                        n_list = {'d': 2, 'e': 1, 'f': 3}
                        self.assertRaises(KeyError, max_integer, my_list)

                    def testDict(self):
                        n_list = {0: 'b', 1: 'a', 2: 'r'}
                        self.assertEqual(max_integer(my_list), 'r')

if __name__ == '__main__':
    unittest.main()
