"""
Tests for pyTona, as per the requirements listed.
"""
from pyTona.main import Interface
from unittest import TestCase
from ReqTracer import requirements
import pyTona.answer_funcs as answer
import getpass
import subprocess
import mock
import socket
import random


def mutate_test(func, *args, **kwargs):
    """
    Best I can think of for messing with data mutation.
    """
    mutate_test.functions = {}

    if func in mutate_test.functions:
        return None
    else:
        mutate_test.functions[func] = None
        return func(*args, **kwargs)

class TestPyTonaFunctions(TestCase):

    """
    QMARK is merely a variable to represent a question mark through ASCII
    """
    
    QMARK = chr(0x3F)

    def tearDown(self):
        if answer.seq_finder:
            answer.seq_finder.stop()

    @requirements(['#0001'])
    def test_string_acceptance(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Who invented Python' + self.QMARK), 'Guido Rossum(BDFL)')

        with self.assertRaises(Exception) as e:
            test_interface.ask(1000)

        self.assertEqual(e.exception.message, 'Not A String!')

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
        self.assertEqual(test_interface.ask('What is 5280 feet in miles' + self.QMARK), str(float(5280) / 5280) + ' miles')

    @requirements(['#0008'])
    def test_valid_match(self):
        test_interface = Interface()
        shutoff = mutate_test(test_interface.ask, 'Why don\'t you shutdown' + self.QMARK)
        self.assertEqual(shutoff, "I'm afraid I can't do that {0}".format(getpass.getuser()))

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
        self.assertEqual(test_interface.correct(), 'Please ask a question first')

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

        test_interface.ask('What is the answer to life, the universe, and everything' + self.QMARK)
        test_interface.teach('42')
        self.assertEqual(test_interface.question_answers[test_interface.last_question].value, '42')

    @requirements(['#0017'])
    def test_feet_to_miles(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('What is 10560 feet in miles' + self.QMARK), '2.0 miles')

    """
    @requirements(['#0018'])
    def test_seconds_passed_question(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('How many seconds since 12' + self.QMARK), '3600')
    """

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

    @requirements(['#0022'])
    def test_get_git_branch(self):
        test_interface = Interface()
        output = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        output = output.strip()
        self.assertEqual(test_interface.ask('Where am I' + self.QMARK), output)

    @requirements(['#0022'])
    def test_fail_get_git_branch(self):
        test_interface = Interface()
        m = mock.Mock()
        m.return_value = [False]

        temp_var = subprocess.Popen.communicate
        subprocess.Popen.communicate = m
        self.assertEqual(test_interface.ask('Where am I' + self.QMARK), 'Unknown')

        m.side_effect = subprocess.CalledProcessError
        self.assertEqual(test_interface.ask('Where am I' + self.QMARK), 'Unknown')

        subprocess.Popen.communicate = temp_var

    @requirements(['#0023'])
    def test_get_git_url(self):
        test_interface = Interface()
        output = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'])
        output = output.strip()
        self.assertEqual(test_interface.ask('Where are you' + self.QMARK), output)

    @requirements(['#0023'])
    def test_fail_get_git_url(self):
        test_interface = Interface()
        m = mock.Mock()
        m.return_value = [False]

        temp_var = subprocess.Popen.communicate
        subprocess.Popen.communicate = m
        self.assertEqual(test_interface.ask('Where are you' + self.QMARK), 'Unknown')

        m.side_effect = subprocess.CalledProcessError
        self.assertEqual(test_interface.ask('Where are you' + self.QMARK), 'Unknown')

        subprocess.Popen.communicate = temp_var

    @requirements(['#0024', '#0025', '#0026'])
    def test_get_users(self):
        test_interface = Interface()

        with mock.patch('socket.socket') as m:
            trial = m.return_value
            trial.connect.return_value = None
            trial.send.return_value = None
            trial.recv.return_value = "Harry$Gary$Mary"

            self.assertEqual(test_interface.ask('Who else is here' + self.QMARK), ['Harry', 'Gary', 'Mary'])
            trial.send.assert_called_with('Who?')
            trial.connect.assert_called_with(('192.168.64.3', '1337'))

    @requirements(['#0024', '#0025', '#0027'])
    def test_get_users_fail(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('Who else is here' + self.QMARK), "IT'S A TRAAAPPPP")

    @requirements(['#0028'])
    def test_get_fib_num(self):
        test_interface = Interface()
        self.assertEqual(test_interface.ask('What is the 1 digit of the Fibonacci sequence' + self.QMARK), 1)

    @requirements(['#0029'])
    def test_get_fib_fail_response(self):
        test_interface = Interface()

        m = mock.Mock(return_value=0)

        random.randint = m

        test0 = test_interface.ask('What is the 1000000 digit of the Fibonacci sequence' + self.QMARK)
        m.return_value = 1
        test1 = test_interface.ask('What is the 1000000 digit of the Fibonacci sequence' + self.QMARK)
        m.return_value = 3
        test3 = test_interface.ask('What is the 1000000 digit of the Fibonacci sequence' + self.QMARK)
        m.return_value = 6
        test6 = test_interface.ask('What is the 1000000 digit of the Fibonacci sequence' + self.QMARK)
        m.return_value = 9
        test9 = test_interface.ask('What is the 1000000 digit of the Fibonacci sequence' + self.QMARK)

        self.assertEqual(test0, 'cool your jets')
        self.assertEqual(test1, 'cool your jets')
        self.assertEqual(test3, 'cool your jets')
        self.assertEqual(test6, 'One second')
        self.assertEqual(test9, 'Thinking...')

