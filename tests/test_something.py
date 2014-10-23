"""
This is the template file for creating unittests.

class TestCase

    methods:
        setUp()
        tearDown()
        skipTest(msg:string)
        fail(msg:string)
        id():string
        # (Actually the docstring of each test_* method)
        shortDescription():string

    assertion methods:
        assertTrue(a, M)
        assertFalse(a, M)
        assertEqual(a, b, M)
        assertNotEqual(a, b, M)
        assertIs(a, b, M)
        assertIsNot(a, b, M)
        assertIsNone(a, M)
        assertIsNotNone(a, M)
        assertIsInstance(a, b, M)
        assertIsNotInstance(a, b, M)

        assertGreater(a, b, M)
        assertLess(a, b, M)
        assertGreaterEqual(a, b, M)
        assertLessEqual(a, b, M)
        assertAlmostEqual(a, b, n, M)
        assertNotAlmostEqual(a, b, n, M)
        assertItemsEqual(a, b, M)

        assertIn(a, b, M)
        assertNotIn(a, b, M)
        assertDictContainsSubset(a, b, M)
        assertDictEqual(a, b, M)
        assertListEqual(a, b, M)
        assertSetEqual(a, b, M)
        assertSequenceEqual(a, b, M)
        assertTupleEqual(a, b, M)
        assertMultilineEqual(a, b, M)
"""
import unittest


class TestSomething(unittest.TestCase):
    """A general testing class must be subclassing unittest.TestCase"""

    def setUp(self):
        """The initialization method running first."""
        pass

    def tearDown(self):
        """The method running last. Ideal for throwing away rubbish."""
        pass

    def test_something_particular(self):
        """A simple/sample testcase."""
        i = 1
        self.assertEqual(i, 1)

if __name__ == '__main__':
    """The following code helps the test unittests to get discovered."""
    unittest.main()
