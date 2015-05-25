Manual Tests
------------

The following tests assume the program is already open.

**Test 0001**

*Setup*

N/A

*Procedure*

#. Look at the title of the window
#. Check that it reads "SharpTona"

-----

**Test 0002**

*Setup*

N/A

*Procedure*

#. Look at the primary area of the application window
#. Check that there is a question label
#. Check that there is an answer label

-----

**Test 0003**

*Setup*

N/A

*Procedure*

#. Check that there is a box to type a question in (next to "Question" label)
#. Check that there is an "Ask" button that the user can interact with

-----

**Test 0004**

*Setup*

#. Type "What is the answer to everything?" into the question field

*Procedure*

#. Click the "Ask" button
#. Check that the answer box reads "42"

-----

**Test 0005**

*Setup*

#. Restart the application

*Procedure*

#. Check that the answer box is shown, but disabled
#. Check that the "Teach" button is shown, but disabled
#. Check that the "Correct" button is shown, but disabled

-----

**Test 0006**

*Setup*

#. Ask any question

*Procedure*

#. Check that some answer appeared in the answer box

-----

**Test 0007**

*Setup*

#. Empty the question field

*Procedure*

#. Click the "Ask" button
#. Check that the answer box reads "Was that a question?"

-----


**Test 0008**

*Setup*

#. Type an already known question in the question field

*Procedure*

#. Click the "Ask" button
#. Check that the answer box reads the correct answer
#. Check that the answer box, "Teach" button, and "Correct" button become enabled

-----

**Test 0009**

*Setup*

#. Build off of the last test (continue from the last step)

*Procedure*

#. Enter a new answer in the answer box
#. Click the "Correct" button
#. Check that the answer box, "Teach" button, and "Correct" button become disabled
#. Enter the same question used previously in the question field
#. Click the "Ask" button
#. Check that the answer display is the corrected answer

-----

**Test 0010**

*Setup*

#. Enter an unknown question in the question field

*Procedure*

#. Click the "Ask" button
#. Check that the answer box reads "I don't know please teach me."
#. Check that the "Teach" button is enabled

-----

**Test 0011**

*Setup*

#. Build off of the last test (continue from the last step)

*Procedure*

#. Enter a suitable answer to the unknown question in the answer box
#. Click the "Teach" button
#. Check that the answer box, "Teach" button, and "Correct" button are disabled
#. Enter the previously unknown question in the question field
#. Click the "Ask" button
#. Check that the answer display is the taught answer