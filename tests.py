import unittest
from unittest.case import TestCase

from stack_classes import PositiveNumberStack, NegativeNumberStack


class PositiveNumberStackClassTest(unittest.TestCase):

    def test_push_stack(self):
        my_stack = PositiveNumberStack()
        my_stack.push(32)
        self.assertEqual(my_stack.size(), 1)
        my_stack.push(47)
        self.assertEqual(my_stack.size(), 2)

    def test_pop_stack(self):
        my_stack = PositiveNumberStack()
        my_stack.push(32)
        self.assertEqual(my_stack.size(), 1)
        my_stack.pop()
        self.assertEqual(my_stack.size(), 0)

    def test_pop_return_value(self):
        my_stack = PositiveNumberStack()
        my_stack.push(32)
        self.assertEqual(my_stack.size(), 1)
        self.assertEqual(my_stack.pop(), 32)

    def test_pop_on_empty_stack(self):
        my_stack = PositiveNumberStack()
        with self.assertRaises(ValueError):
            my_stack.pop()

    def test_push_negative_number(self):
        my_stack = PositiveNumberStack()
        with self.assertRaises(ValueError):
            my_stack.push(-1)

    def test_max_size(self):
        my_stack = PositiveNumberStack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        with self.assertRaises(ValueError):
            my_stack.push(4)

    def test_str_method(self):
        my_stack = PositiveNumberStack()
        my_stack.push(1)
        self.assertEqual(str(my_stack), "Stack with 1 object(s)")


class NegativeNumberStackClassTest(TestCase):

    def test_push_positive_number(self):
        my_stack = NegativeNumberStack()
        with self.assertRaises(ValueError):
            my_stack.push(1)
        my_stack.push(-1)
        my_stack.push(-2)
        my_stack.push(-3)
        self.assertEqual(my_stack.pop(), -3)
        self.assertEqual(my_stack.pop(), -2)
        self.assertEqual(my_stack.pop(), -1)
        with self.assertRaises(ValueError):
            self.assertEqual(my_stack.pop())
        self.assertEqual(str(my_stack), "Stack with 0 object(s)")

if __name__ == "__main__":
    unittest.main()
