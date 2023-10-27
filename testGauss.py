import numpy.testing as npt
from GaussSeidelAlgorithm import *
import unittest
class testGauss(unittest.TestCase):
    def testDeterminedEquations1(self):
        matrix = np.array([[6, 4, -1], [2, 5, 1], [-1, -1, 4]])
        vector = np.array([5, 4, -5])
        npt.assert_array_almost_equal(gaussSeidel(matrix, vector, 0.0000001, 10000),
                                      np.array([0, 1, -1]), decimal=7)

    def testDeterminedEquations2(self):
        matrix = np.array([[2, 1, -1], [1, -1, -1], [2, 2, 1]])
        vector = np.array([1, 3, 1])
        npt.assert_array_almost_equal(gaussSeidel(matrix, vector, 0.0000001, 10000),
                                      np.array([2, -2, 1]), decimal=7)

    def testDeterminedEquations3(self):
        matrix = np.array([[4, 1, 0], [1, 4, 1], [0, 1, 4]])
        vector = np.array([15, 10, 5])
        npt.assert_array_almost_equal(gaussSeidel(matrix, vector, 1e-7, 10000),
                                      np.array([95/28, 10/7, 25/28]), decimal=7)

    def testDeterminedEquationsLong(self):
        matrix = np.array([[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0,
                                                                                1, 0,
                                                                                0, 0,
                                                                                0,
                                                                                0],
                           [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0,
                                                                                0, 0,
                                                                                0, 1,
                                                                                0,
                                                                                0],
                           [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]])
        vector = np.array([5, 7, 8, 2, 1, 5, 10, 9])

        npt.assert_array_almost_equal(gaussSeidel(matrix, vector, 0.0000001, 100),
                                      np.array([5, 7, 8, 2, 1, 5, 10, 9]))

    def test_zero_diagonal(self):
        matrix = np.array([[0, 1], [1, 0]])
        vector = np.array([1, 1])

        with self.assertRaises(ValueError):
            gaussSeidel(matrix, vector, 0.0000001, 100)



