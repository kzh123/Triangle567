# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidTriangleA(self):
        self.assertEqual(classifyTriangle(201, 201, 201), "InvalidInput", "201,201,201 should return Invalid input")

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(0, 0, 0), "InvalidInput")

    def testNotInt(self):
        self.assertEqual(classifyTriangle(1.3, 1.3, 1.3), "InvalidInput")

    def testIsoceles(self):
        self.assertEqual(classifyTriangle(1, 2, 2), "Isoceles")

    def testScalene(self):
        self.assertEqual(classifyTriangle(2, 3, 4), "Scalene")

    def testNotTran(self):
        self.assertEqual(classifyTriangle(1, 1, 2), "NotATriangle")

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
