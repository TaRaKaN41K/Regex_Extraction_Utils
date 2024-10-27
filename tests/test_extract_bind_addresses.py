import unittest
from src.find_bind_ip import extract_bind_addresses
from test_cases.test_cases_extract_bind_addresses import test_cases


class TestExtractBindAddresses(unittest.TestCase):
    @staticmethod
    def print_result(input_str, result):
        print(f'Input:\n{input_str}\n'
              f'Output: {result}\n')

    def test_bind_addresses(self):
        for config_str, expected in test_cases:
            with self.subTest(config_str=config_str, expected=expected):
                result = extract_bind_addresses(config_str)
                self.print_result(config_str, result)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
