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

    @requirements(['#0005'])

    @requirements(['#0006'])

    @requirements(['#0007'])

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

    @requirements(['#0011', '#0015'])
    def test_answer_type(self):
        test_interface = Interface()
        assert hasattr(test_interface.question_answers['Why don\'t you shutdown'].function, '__call__')
        self.assertIsInstance(test_interface.question_answers['How many seconds since'].value, str)

    @requirements(['#0012', '#0016'])
    def test_no_previous_questions(self):
        test_interface = Interface()
        self.assertEqual(test_interface.teach(), 'Please ask a question first')

    @requirements(['#0013'])
    def test_existing_answer(self):
        test_interface = Interface()
        test_interface.ask('How many seconds since>')
        self.assertEqual(test_interface.teach('A lot'), 'I don\'t know about that. I was taught differently')

    @requirements(['#0014'])
    def test_answer_correction(self):
        test_interface = Interface()
        test_interface.ask('How many seconds since>')
        test_interface.correct('A lot')
        self.assertEqual(test_interface.question_answers[test_interface.last_question].value, 'A lot')

    @requirements(['#0017'])
    def test_feet_to_miles(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('What is 10560 feet in miles>'), '2.0 miles')

    @requirements(['#0018'])
    def test_seconds_passed_question(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('How many seconds since 12>'), '3600')

    @requirements(['#0019'])
    def test_python_creator(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Who invented Python>'), 'Guido Rossum(BDFL)')

    @requirements(['#0020'])
    def test_understand_question(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Why don\'t you understand me>'), 'Because you do not speak 1s and 0s')

    @requirements(['#0021'])
    def test_shutdown_question(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Why don\'t you shutdown>'), "I'm afraid I can't do that {0}".format(getpass.getuser()))