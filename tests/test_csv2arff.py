import os
import unittest
import tempfile
import difflib
import csv2arff


class TestCsv2Arff(unittest.TestCase):

    def setUp(self):
        local_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_path = os.path.join(local_dir)
        self.csv1 = '''foo,bar,class
1,2,A
3,4,B
'''

    def expectedCsv1(self, filename):
        ret = """@relation %s

@attribute foo numeric
@attribute bar numeric
@attribute class {'A','B'}
@data
1,2,'A'
3,4,'B'""" % (filename)
        return ret

    def test_simple(self):
        tmpIn = tempfile.mkstemp()[1]
        tmpOut = tempfile.mkstemp()[1]
        try:
            self.writeContent(tmpIn, self.csv1)

            csv2arff.Csv2Arff(tmpIn, tmpOut)
            self.assertFileConent(self.expectedCsv1(tmpOut), tmpOut)
        finally:
            os.remove(tmpIn)

    def assertFileConent(self, expected, b, msg=None):
        """Assert that two files are equal.

        If they aren't, show a nice diff.

        """
        second = open(b).read()
        self.assertTrue(isinstance(expected, str),
                        'First argument is not a string')
        self.assertTrue(isinstance(second, str),
                        'Second argument is not a string')

        if expected != second:
            message = ''.join(difflib.ndiff(expected.splitlines(True),
                                            second.splitlines(True)))
            if msg:
                message += " : " + msg
            self.fail("Files are different:\n" + message)

    def writeContent(self, filename, text):
        f = open(os.path.join(self.base_path, filename), 'w')
        f.write(text)
        f.close()

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
