"""
Tests for pyTona, as per the requirements listed.
"""
from pyTona.main import Interface
from unittest import TestCase
from ReqTracer import requirements
import getpass


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

    @requirements(['#0008'])
    def test_valid_match(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Why don\'t you shutdown>'), "I'm afraid I can't do that {0}".format(getpass.getuser()))

    @requirements(['#0009'])
    def test_invalid_match(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('How does this work>'), "I don't know, please provide the answer")

    @requirements(['#0010'])
    def test_previous_question(self):
        test_interface = Interface()
        test_interface.ask('How many seconds since>')
        self.assertEqual(test_interface.last_question, 'How many seconds since')

    @requirements(['#0012'])
    def test_no_previous_questions(self):
        test_interface = Interface()
        self.assertEqual(test_interface.teach(), 'Please ask a question first')

    @requirements(['#0013'])
    def test_existing_answer(self):
        test_interface = Interface()
        test_interface.ask('How many seconds since>')
        self.assertEqual(test_interface.teach('A lot'), 'I don\'t know about that. I was taught differently')

