"""
Round 1: Meant to test the Orc defense system
"""
from source.orc_defense import orc_defense_system
from unittest import TestCase

class TestDefenses(TestCase):

    def test_breach_alarm(self):
        result = orc_defense_system(10, 200)
        self.assertEqual(result, 'Perimeter Breach')

    def test_quit(self):
        with self.assertRaises(SystemExit) as cm:
            orc_defense_system(10, 300, 'X')
        self.assertEqual(cm.exception.code, 1)

    def test_distance_indicator(self):
        result = orc_defense_system(10, 300, 'D')
        self.assertEqual(result, 300)

    def test_speed_indicator(self):
        result = orc_defense_system(10, 300, 'S')
        self.assertEqual(result, 10)
