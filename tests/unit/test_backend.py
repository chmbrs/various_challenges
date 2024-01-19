import unittest
from unittest import IsolatedAsyncioTestCase

from src.backend import find_duplicated_items
from src.backend import progressive_delay_item_writer
from src.backend import closed_brackets_checker


class TestBackend(unittest.TestCase):
    def test_find_duplicated_items(self):
        data = [1, 2, 3, 2, 4, 5, 6, 4]
        result = find_duplicated_items(data)
        self.assertEqual(result, [2, 4])

    def test_find_duplicated_items(self):
        data = ['a', 'b', 'c', 'd', 'c', 'a']
        result = find_duplicated_items(data)
        self.assertEqual(result, ['a', 'c'])

    def test_closed_brackets_checker(self):
        brackets_input_true = '{[]}'
        brackets_output_false = '{(])}'
        brackets_output_false_1 = '{([)]}'

        self.assertTrue(closed_brackets_checker(brackets_input_true))
        self.assertFalse(closed_brackets_checker(brackets_output_false))
        self.assertFalse(closed_brackets_checker(brackets_output_false_1))


class AsyncTest(IsolatedAsyncioTestCase):

    async def test_progressive_delay_item_writer(self):
        data = ["A", "B", "C", "D", "E"]
        result = await progressive_delay_item_writer(data)
        self.assertEqual([('A', 1), ('B', 2), ('C', 4), ('D', 8), ('E', 16)], result)


if __name__ == '__main__':
    unittest.main()