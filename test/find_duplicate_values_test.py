import unittest
from find_duplicate_values import find_duplicate_values
import pycodestyle

class TestFindDuplicateValues(unittest.TestCase):

    def test_no_dupes(self):
        expected = []
        input = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(expected, find_duplicate_values(input))

    def test_one_dupe(self):
        expected = [2]
        input = {'a': 1, 'b': 2, 'c': 2, 'd': 4}
        self.assertEqual(expected, find_duplicate_values(input))

    def test_many_dupes(self):
        expected = ['1', '2']
        input = {'a': '1', 'b': '1', 'c': '2', 'd': '1', 'e': '2'}
        self.assertEqual(expected, sorted(find_duplicate_values(input)))

    def test_many_dupes_ints(self):
        expected = [1, 2, 3]
        input = {'a': 1, 
                 'b': 1, 
                 'c': 2, 
                 'd': 2, 
                 'e': 3,
                 'f': 3,
                 'g': 4
                 }
        self.assertEqual(expected, sorted(find_duplicate_values(input)))

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['convert_to_dictionary.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
