from pywinauto import application
import os
import random
import time

IGNORED_BUGS = [
        # 'You found bug 1', 
        # 'You found bug 2', 
        # 'You found bug 3', 
        # 'You found bug 4', 
        # 'You found bug 5', 
        # 'You found bug 6', 
        # 'You found bug 7'
        ]

KNOWN_QUESTION_ANSWERS = {"What is the answer to everything?": "42"}

VALID_CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ',
               '?', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

NUM_VALID_CHARS = len(VALID_CHARS) - 1
               
def check_for_bug(app):
    if "You found bug" in app.sharpTona['Answer:Edit'].Texts()[0]:
        if app.sharpTona['Answer:Edit'].Texts()[0] not in IGNORED_BUGS:
            print "BUG FOUND: {0}".format(app.sharpTona['Answer:Edit'].Texts()[0])
            return True
    return False
    
def ask_question(app, question=None):
    if app.sharpTona['Ask'].IsEnabled():
        question_len = random.randint(0, 60)
        if question is None:
            question = "".join(VALID_CHARS[random.randint(0, NUM_VALID_CHARS)] for x in range(question_len))
        print "Ask: {0}".format(question)
        app.sharpTona['Question:Edit'].SetText(question)
        app.sharpTona['Ask'].Click()
        
def teach(app):
    if app.sharpTona['Teach'].IsEnabled():
        answer_len = random.randint(0, 60)
        answer = "".join(VALID_CHARS[random.randint(0, NUM_VALID_CHARS)] for x in range(answer_len))
        print "Teach: {0}".format(answer)
        app.sharpTona['Answer:Edit'].SetText(answer)
        app.sharpTona['Teach'].Click()
        KNOWN_QUESTION_ANSWERS[app.sharpTona['Question:Edit'].Texts()[0]] = answer
    else:
        num_question =  len(KNOWN_QUESTION_ANSWERS.keys())
        random_question = KNOWN_QUESTION_ANSWERS.keys()[random.randint(0, num_question - 1)]
        question = random_question
        ask_question(app, question)
        if app.sharpTona['Answer:Edit'].Texts()[0] != KNOWN_QUESTION_ANSWERS[question]:
            print "Unexpected answer to question {0} - {1}".format(question, app.sharpTona['Answer:Edit'].Texts()[0])
        
def correct(app):
    if app.sharpTona['Correct'].IsEnabled():
        answer_len = random.randint(0, 60)
        answer = "".join(VALID_CHARS[random.randint(0, NUM_VALID_CHARS)] for x in range(answer_len))
        print "Correct: {0}".format(answer)
        app.sharpTona['Answer:Edit'].SetText(answer)
        app.sharpTona['Correct'].Click()
        KNOWN_QUESTION_ANSWERS[app.sharpTona['Question:Edit'].Texts()[0]] = answer
    else:
        num_question =  len(KNOWN_QUESTION_ANSWERS.keys())
        random_question = KNOWN_QUESTION_ANSWERS.keys()[random.randint(0, num_question - 1)]
        question = random_question
        ask_question(app, question)
        if app.sharpTona['Answer:Edit'].Texts()[0] != KNOWN_QUESTION_ANSWERS[question]:
            print "Unexpected answer to question {0} - {1}".format(question, app.sharpTona['Answer:Edit'].Texts()[0])

def main():

    bug_found = False
    
    app = application.Application()
    app.start('SharpTona.exe')
    
    bug_found = check_for_bug(app)
    while not bug_found:
        index = random.randint(0, 3)
        
        if index == 0:
            ask_question(app)
        elif index == 1:
            teach(app)
        else:
            correct(app)
        #time.sleep(.5)
        bug_found = check_for_bug(app)
        
    app.sharpTona.Close()

if __name__ == "__main__":
    if os.path.exists('sharpTona.exe'):
        main()
        
    else:
        print "Could not find 'sharpTona.exe'"
