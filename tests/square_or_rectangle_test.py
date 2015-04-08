"""
Test for square_or_rectangle
"""
from source.square_or_rectangle import determine_square_or_rectangle
from unittest import TestCase

class TestDetermineSquareOrRectangle(TestCase):

	def test_if_square_all_int(self):
                result = determine_square_or_rectangle(2, 2, 2, 2)
		self.assertEqual(result, 'square')

	def test_if_rectangle_all_int(self):
                result = determine_square_or_rectangle(1, 1, 3, 3)
                self.assertEqual(result, 'rectangle')

        def test_side_less_than_zero(self):
                result = determine_square_or_rectangle(0, 1, 1, 1)
                self.assertEqual(result, 'invalid')

        def test_if_variables_numeric(self):
                result = determine_square_or_rectangle('a', 1, 1, 1)
                self.assertEqual(result, 'invalid')
                
