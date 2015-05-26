import pywinauto
import time
import SendKeys
from pywinauto import application, controls
from unittest import TestCase


class TestSharpTonaUI(TestCase):
    app = None

    def setUp(self):
        self.app = application.Application()
        self.app.start_("SharpTona.exe")
        self.sharp = self.app.SharpTona

    def tearDown(self):
        self.app.SharpTona.TypeKeys("%{F4}")
        self.app = None

    def test_title(self):
        # Requirement 0001
        self.assertEqual(self.sharp.WindowText(), "SharpTona")

    def test_question_answer_labels(self):
        # Requirement 0002
        self.assertIsNotNone(self.sharp["Question:"])
        self.assertIsNotNone(self.sharp["Answer:"])

    def test_question_box_ask_button(self):
        # Requirement 0003
        self.assertEqual(self.sharp["Question:Edit"].friendlyclassname, "Edit")
        self.assertEqual(self.sharp["Ask"].friendlyclassname, "Button")

    def test_everything_question(self):
        # Requirements 0004 and 0006
        self.sharp["Question:Edit"].SetFocus()
        self.sharp["Question:Edit"].TypeKeys("What is the answer to everything?", with_spaces=True)
        self.sharp["Ask"].Click()
        self.assertEqual(self.sharp["Answer: Edit"].Texts()[0], "42")

    def test_disabled_by_default(self):
        # Requirement 0005
        self.assertFalse(self.sharp["Answer:Edit"].IsEnabled())
        self.assertFalse(self.sharp["Teach"].IsEnabled())
        self.assertFalse(self.sharp["Correct"].IsEnabled())

    def test_is_a_question(self):
        # Requirement 0007
        self.sharp["Ask"].Click()
        self.assertEqual(self.sharp["Answer: Edit"].Texts()[0], "Was that a question?")

    def test_click_correct_disable_all(self):
        # Requirements 0008 and 0009
        self.sharp["Question:Edit"].TypeKeys("What is the answer to everything?", with_spaces=True)
        self.sharp["Ask"].Click()
        # Change the known answer to something new
        self.sharp["Answer:Edit"].SetFocus()
        self.sharp["Answer:Edit"].TypeKeys("No clue", with_spaces=True)
        self.sharp["Correct"].Click()
        # Check that things disable
        self.assertFalse(self.sharp["Answer:Edit"].IsEnabled())
        self.assertFalse(self.sharp["Teach"].IsEnabled())
        self.assertFalse(self.sharp["Correct"].IsEnabled())
        # Check that the answer was stored properly
        self.sharp["Ask"].Click()
        self.assertEqual(self.sharp["Answer:Edit"].Texts()[0], "No clue")
        self.assertTrue(self.sharp["Answer:Edit"].IsEnabled())

    def test_unknown_question(self):
        # Requirements 0010 and 0011
        self.sharp["Question:Edit"].TypeKeys("Where am I?", with_spaces=True)
        self.sharp["Ask"].Click()
        # Check that the system outputs an unknown question response
        self.assertEqual(self.sharp["Answer:Edit"].Texts()[0], "I don't know please teach me.")
        # Check that the teach button gets enabled
        self.assertTrue(self.sharp["Teach"].IsEnabled())
        self.assertFalse(self.sharp["Correct"].IsEnabled())
        # Teach the system an answer
        self.sharp["Answer:Edit"].TypeKeys("Earth would be a good guess", with_spaces=True)
        self.sharp["Teach"].Click()
        # Check that things disable
        self.assertFalse(self.sharp["Answer:Edit"].IsEnabled())
        self.assertFalse(self.sharp["Teach"].IsEnabled())
        self.assertFalse(self.sharp["Correct"].IsEnabled())
        # Check that the answer was stored properly
        self.sharp["Ask"].Click()
        self.assertEqual(self.sharp["Answer:Edit"].Texts()[0], "Earth would be a good guess")
        self.assertTrue(self.sharp["Answer:Edit"].IsEnabled())