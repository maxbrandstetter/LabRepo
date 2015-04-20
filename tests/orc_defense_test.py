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

    def test_show_options(self):
        result = orc_defense_system(10, 300, '?')
        self.assertTrue(result)

    def test_orc_types(self):
        result = orc_defense_system(10, 300, 'T', 4)
        self.assertEqual(result, 4)

    def test_orc_removal(self):
        result = orc_defense_system(10, 300, 'R')
        self.assertEqual(result, 'Target Removed')

    def test_alternate_units_imperial(self):
        result = orc_defense_system(10, 300, 'S', 1, 'imperial')
        self.assertEqual(result, 32.8)

    def test_alternate_units_parsec(self):
        result = orc_defense_system(10, 300, 'S', 1, 'parsec')
        self.assertEqual(result, 3.24*10**-16)

    def test_alternate_units_nautical(self):
        result = orc_defense_system(10, 300, 'S', 1, 'nautical')
        self.assertEqual(result, 19.4)

    def test_set_priority(self):
        result = orc_defense_system(10, 300, 'P')
        self.assertEqual(result, 2)

    def test_orc_identification(self):
        result = orc_defense_system(10, 300, 'F')
        self.assertEqual(result, 'Details Given')

    def test_orc_generation(self):
        result = orc_defense_system(10, 300, 'G')
        self.assertTrue(result)

    def test_remove_all_orcs(self):
        result = orc_defense_system(10, 300, 'ENTer the Trees')
        self.assertEqual(result, [])
        
        
        
