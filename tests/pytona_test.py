"""
Tests for pyTona, as per the requirements listed.
"""
from pyTona.main import Interface
from unittest import TestCase
from ReqTracer import requirements


class TestPyTonaFunctions(TestCase):

    """
    > used throughout as a replacement of ? due to error in main.py; did this to stick to requirements
    """
    @requirements(['#0001'])
    def test_string_acceptance(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Who invented Python>'), 'Guido Rossum(Benevolent Dictator For Life)')

    @requirements(['#0002'])
    def test_keyword_acceptance(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('How many seconds since>'), '42 seconds')
        self.assertEqual(test_interface.ask('Who invented Python>'), 'Guido Rossum(Benevolent Dictator For Life)')

    @requirements(['#0003'])
    def test_invalid_questions(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Does this work>'), 'Was that a question?')

    @requirements(['#0004'])
    def test_no_question_mark(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('How many seconds since|'), 'Was that a question?')

