import unittest
from convert_to_dictionary import convert_to_dictionary
import pycodestyle

class TestConvertToDictionary(unittest.TestCase):

    def test_str_int(self):
        expected = {'a': 1, 'b': 2}
        list1 = ['a', 'b']
        list2 = [1, 2]
        self.assertEqual(expected, convert_to_dictionary(list1, list2))

    def test_str_str(self):
        expected = {'a': 'z', 'b': 'y'}
        list1 = ['a', 'b']
        list2 = ['z', 'y']
        self.assertEqual(expected, convert_to_dictionary(list1, list2))

    def test_mismatched_list_length(self):
        list1 = ['a', 'b', 'c']
        list2 = ['z', 'y']
        self.assertRaises(ValueError, convert_to_dictionary, list1, list2)

    def test_duplicate_key(self):
        list1 = ['a', 'b', 'a']
        list2 = ['z', 'y', 'x']
        self.assertRaises(ValueError, convert_to_dictionary, list1, list2)

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['convert_to_dictionary.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
