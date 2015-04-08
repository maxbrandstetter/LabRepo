"""
Test for source.source1
"""
from source.source1 import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1, 2, 1)
        self.assertEqual(result, 'isosceles')

    def test_check_not_zero(self):
        result = get_triangle_type(0, 1, 1)
        self.assertEqual(result, 'invalid')

    def test_check_sides_numeric(self):
        result = get_triangle_type('a', 1, 1)
        self.assertEqual(result, 'invalid')

    def test_if_a_is_dict_scalene(self):
        a = dict(one=1, two=2, three=3)
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_if_a_is_tuple_scalene(self):
        a = tuple([1, 2, 3])
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')
