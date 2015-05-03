"""
Tests for pyTona, as per the requirements listed.
"""
from pyTona.main import Interface
from unittest import TestCase
from ReqTracer import requirements
import getpass

class TestPyTonaFunctions(TestCase):

    """
    QMARK is merely a variable to represent a question mark through ASCII
    """
    
    QMARK = chr(0x3E)
    
    @requirements(['#0001'])
    def test_string_acceptance(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Who invented Python' + self.QMARK), 'Guido Rossum(Benevolent Dictator For Life)')

    @requirements(['#0002', '#0003'])
    def test_keyword_acceptance(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Does this work' + self.QMARK), 'Was that a question?')

    @requirements(['#0004'])
    def test_no_question_mark(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('This isn\'t a question.'), 'Was that a question?')

    @requirements(['#0005'])
    def test_spacing_fail(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Whydoesthisnotwork' + self.QMARK), 'Was that a question?')

    @requirements(['#0006'])
    def test_90_match(self):
        test_interface = Interface()
        q100 = 'What is 5280 feet in miles' + self.QMARK
        q90 = 'What 5280 feet in miles' + self.QMARK
        q90_no_units = 'What is 5280 in miles' + self.QMARK

        self.assertEqual(test_interface.ask(q100), str(float(5280) / 5280) + ' miles')
        self.assertEqual(test_interface.ask(q90), str(float(5280 / 5280)) + ' miles')
        self.assertEqual(test_interface.ask(q90_no_units), "I don't know, please provide the answer")

    @requirements(['#0007'])
    def test_number_detection(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('What is 5280 feet in miles' + self.QMARK), str(float(5280) / 5280))

    @requirements(['#0008'])
    def test_valid_match(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Why don\'t you shutdown' + self.QMARK), "I'm afraid I can't do that {0}".format(getpass.getuser()))

    @requirements(['#0009'])
    def test_invalid_match(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('How does this work' + self.QMARK), "I don't know, please provide the answer")

    @requirements(['#0010'])
    def test_previous_question(self):
        test_interface = Interface()
        test_interface.ask('How many seconds since' + self.QMARK)
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
        test_interface.ask('How many seconds since' + self.QMARK)
        self.assertEqual(test_interface.teach('A lot'), 'I don\'t know about that. I was taught differently')

    @requirements(['#0014'])
    def test_answer_correction(self):
        test_interface = Interface()
        test_interface.ask('How many seconds since' + self.QMARK)
        test_interface.correct('A lot')
        self.assertEqual(test_interface.question_answers[test_interface.last_question].value, 'A lot')

    @requirements(['#0017'])
    def test_feet_to_miles(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('What is 10560 feet in miles' + self.QMARK), '2.0 miles')

    @requirements(['#0018'])
    def test_seconds_passed_question(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('How many seconds since 12' + self.QMARK), '3600')

    @requirements(['#0019'])
    def test_python_creator(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Who invented Python' + self.QMARK), 'Guido Rossum(BDFL)')

    @requirements(['#0020'])
    def test_understand_question(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Why don\'t you understand me' + self.QMARK), 'Because you do not speak 1s and 0s')

    @requirements(['#0021'])
    def test_shutdown_question(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Why don\'t you shutdown' + self.QMARK), "I'm afraid I can't do that {0}".format(getpass.getuser()))