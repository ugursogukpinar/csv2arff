import os
import unittest
import tempfile
import difflib
import csv2arff
from argparse import Namespace


class TestCsv2Arff(unittest.TestCase):

    def setUp(self):
        local_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_path = os.path.join(local_dir)
        self.csv1 = '''foo,bar,class
1,2,A
3,4,B
'''

    def test_simple(self):
        tmpIn = tempfile.mkstemp()[1]
        tmpOut = tempfile.mkstemp()[1]
        try:
            self.writeContent(tmpIn, self.csv1)

            csv2arff.Csv2Arff(Namespace(input=tmpIn, output=tmpOut,
                                        delimiter=','))
            self.assertFileContent(self.expectedCsv1(tmpOut), tmpOut)
        finally:
            os.remove(tmpIn)
            os.remove(tmpOut)

    def test_t1(self):
        fileIn = self.base_path + '/data/t1.csv'
        fileExp = self.base_path + '/data/t1.arff'
        fileOut = tempfile.mkstemp()[1]
        try:
            csv2arff.Csv2Arff(Namespace(input=fileIn, output=fileOut,
                                        name='t1', delimiter=','))
            self.compareFiles(fileExp, fileOut)
        finally:
            os.remove(fileOut)

    def test_t2(self):
        fileIn = self.base_path + '/data/t2.csv'
        fileExp = self.base_path + '/data/t2.arff'
        fileOut = tempfile.mkstemp()[1]
        try:
            csv2arff.Csv2Arff(Namespace(input=fileIn, output=fileOut,
                                        name='t2', delimiter=',',
                                        verbose=True))
            self.compareFiles(fileExp, fileOut)
        finally:
            os.remove(fileOut)

    def test_invalid_args(self):
        with self.assertRaises(SystemExit):
            csv2arff.Csv2Arff(Namespace(input='foo', output='foo'))

    def expectedCsv1(self, filename):
        ret = """@relation %s

@attribute foo numeric
@attribute bar numeric
@attribute class {'A','B'}
@data
1,2,'A'
3,4,'B'""" % (filename)
        return ret

    def diff(self, first, second, msg=None):
        """Assert that two strings are equal.

        If they aren't, show a nice diff.

        """
        self.assertTrue(isinstance(first, str),
                        'First argument is not a string')

        self.assertTrue(isinstance(second, str),
                        'Second argument is not a string')

        if first != second:
            message = ''.join(difflib.ndiff(first.splitlines(True),
                                            second.splitlines(True)))
            if msg:
                message += " : " + msg
            self.fail("Diff:\n" + message)

    def assertFileContent(self, expected, file, msg=None):
        """Assert file content.

        If they aren't, show a nice diff.

        """
        second = open(file).read()

        self.assertTrue(isinstance(second, str),
                        'Second argument is not a string')
        self.diff(expected, second)

    def compareFiles(self, expected, file, msg=None):
        """Compare two files

        If aren't the same, show a nice diff.

        """
        a = open(expected).read()
        b = open(file).read()
        self.diff(a, b)

    def writeContent(self, filename, text):
        f = open(os.path.join(self.base_path, filename), 'w')
        f.write(text)
        f.close()


if __name__ == '__main__':
    unittest.main()
