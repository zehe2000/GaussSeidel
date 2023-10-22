from readEquation import *
import unittest

class testReadEquation(unittest.TestCase):

    def test_AIsMissing(self):
        content = readfile('C:\\Users\\Admin\\Desktop\\uds zeinab\\eigene '
                          'Projekte\\Gauß-Seidel\\test\\brokenTxt\\aIsMissing.txt')
        with self.assertRaises(ValueError):
            convertContentToArray(content)

    def test_BIsMissing(self):
        content = readfile('C:\\Users\\Admin\\Desktop\\uds zeinab\\eigene '
                          'Projekte\\Gauß-Seidel\\test\\brokenTxt\\bIsMissing.txt')
        with self.assertRaises(ValueError):
            convertContentToArray(content)

    def test_DifferentRowLen(self):
        content = readfile('C:\\Users\\Admin\\Desktop\\uds zeinab\\eigene '
                          'Projekte\\Gauß-Seidel\\test\\brokenTxt\\differentRowLen.txt')
        with self.assertRaises(ValueError):
            convertContentToArray(content)

    def test_FalseFormat(self):
        content = readfile('C:\\Users\\Admin\\Desktop\\uds zeinab\\eigene '
                          'Projekte\\Gauß-Seidel\\test\\brokenTxt\\falseFormat.txt')
        with self.assertRaises(ValueError):
            convertContentToArray(content)

    def test_LettersInMatrix(self):
        content = readfile('C:\\Users\\Admin\\Desktop\\uds zeinab\\eigene '
                          'Projekte\\Gauß-Seidel\\test\\brokenTxt\\lettersInMatrix.txt')
        with self.assertRaises(ValueError):
            convertContentToArray(content)

    def test_TwoMatrices(self):
        content = readfile('C:\\Users\\Admin\\Desktop\\uds zeinab\\eigene '
                           'Projekte\\Gauß-Seidel\\test\\brokenTxt\\twoMatrices.txt')
        with self.assertRaises(ValueError):
            convertContentToArray(content)

    def test_VectorIsMissing(self):
        content = readfile('C:\\Users\\Admin\\Desktop\\uds zeinab\\eigene '
                           'Projekte\\Gauß-Seidel\\test\\brokenTxt\\vectorIsMissing'
                           '.txt')
        with self.assertRaises(ValueError):
            convertContentToArray(content)




