import unittest
from src.find_full_path import extract_path
from test_cases.test_cases_extract_path import test_cases


class TestExtractPath(unittest.TestCase):
    @staticmethod
    def print_result(input_str, result):
        print(f'Input:  {input_str}\n'
              f'Output: {result}\n')

    def test_paths(self):
        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str, expected=expected):
                result = extract_path(input_str)
                self.print_result(input_str, result)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
