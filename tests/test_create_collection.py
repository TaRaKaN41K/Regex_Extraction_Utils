import unittest
from src.creating_collection import create_collection
from test_cases.test_cases_create_collection import test_cases


class TestCreateCollection(unittest.TestCase):
    @staticmethod
    def print_result(input_data, result):
        print(f'Input:\n{input_data}\n'
              f'Output: {result}\n')

    def test_create_collection(self):
        for config_str, expected in test_cases:
            with self.subTest(config_str=config_str, expected=expected):
                result = create_collection(config_str)
                self.print_result(config_str, result)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
