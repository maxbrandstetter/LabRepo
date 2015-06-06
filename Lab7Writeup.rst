Lab 7 Writeup
-------------

**What bugs did you find?**

#. Ask a question with more than one character and "?" in the question (may be several) but is NOT at the end. Must not meet Bug 2 or 3's requirements.
#. Ask a question which has a number of characters divisible by 5 (5, 10, 15...)
#. Ask a question with 51 or more characters.  Must not meet the requirements of Bug 2.
#. Occurs once 10 Q/A's have been taught (10 calls to Teach) and stored.
#. When the question "What is the answer to everything?" has an integer answer and is corrected to a string, the bug occurs.  Similarly, if the answer is a string and is corrected to an integer, the bug occurs.
#. Occasionally, sharpTona will entirely fail to open, resulting in bug 6
#. Teach an answer with a "?" somewhere in it.  Length and other characters do not matter.

**What are the advantages and disadvantages of fuzz testing?**

Advantages: Fuzz testing helps to find bugs that would otherwise not be found; random generations means the program must handle something that most users wouldn't think of entering/testing.

Disadvantages: This method of random generation to find bugs that it may take a long time to find the bug and replicate it enough to find it, such as with Bug 6.  Since the bug only occured when the app randomly failed to launch, I had to run the test repeatedly until the error occurred again before I knew what it was.  Only simple bugs will be found in any reasonable amount of time.

**What was the hardest part of this lab?**

Bug 4 seemed odd to start, but ended up being simpler than my initial thoughts.  So, I'd say bug 5 was probably the most difficult.

**How would you apply the concept of fuzz testing to testing a phone? a webpage? a library?**

Phone: Call a bunch of random numbers, test series of random inputs, hit combinations of buttons and such.

Webpage: Enter random data where input is available, click like a madman (click everything everywhere, every nook and cranny), use links in a nonsensical order (?), enter random inputs where available.

Library: I'm assuming this refers to a computer science-y kind of library, not the kind with books; I don't know much, so these are kind of guesses. Use features of the library on those same features (?); if input is available, say for the creation of an object, make it nonsensical; if several functions are available, call them repeatedly or nest them.

**How could throttling fuzz test scripts help with finding bugs?**

Since it narrows down the possibility or "range" of bugs that occur, it may allow for people to find bugs more efficiently.

**What is Delta Debugging and how would it help with fuzz testing?**

Delta Debugging is a process meant to narrow down the problem by making the set in which the problem occurs smaller and smaller.  It isolates bugs as much as possible through automation.

**If steps 1-20 were to produce an error using delta debugging what are the steps that 
would arrive at steps 8, 12, 13, 19 and 20 being necessary to reproduce the error?**

I suppose if we had some complex tree of if/else statements and other loops, and at certain points throughout, a problem function was called, we could isolate the bug by toggling those statements and loops.  By always passing or failing, we could find the exact spots it occurred, hitting those specific blocks/steps sometimes and other times missing them entirely.  Kind of a confusing question, so hopefully my answer makes some sense.
