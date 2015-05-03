Lab 3 Write-Up Max Brandstetter
-------------------------------

What are five examples of other testing(nose2) plugins that might be useful?
============================================================================

#. The ResultReporter plugin may be useful for ease of testing.
#. If running heavily IO or CPU bound tests, using the mp (multiprocessing) plugin could assist in completion time.
#. You could use the attrib plugin to further specify what tests to run.
#. Similarly to the attrib plugin, TestID could be used to paramaterize tests by ID, allowing for more sequential selection.
#. If creating plugins (maybe for the purpose of test assisting), you could use PrintHooks, which creates output of hooks for debugging.

Do you plan to create any of these plugins for your term project?
=================================================================

I may have misinterpreted the above, as it's based on existing plugins, I would say no.  However, for the purpose of debugging, I would likely utilize PrintHooks alongside perhaps a self-made plugin to output some sort of test data.

What is the hardest part of this lab?
=====================================

Personally, creating the nose2 plugin proved a bit unusual and difficult, although the tests which required information only available within functions were similarly awkward.  Definitely had to read up on some documentation and stuff to understand the proper procedure (or what I hope is the proper procedure).

Did the code fully and completely implement the requirements? Explain
=====================================================================

The code did not fully and completely implement the requirements, as there were instances such as with 'How many seconds since' where the requirements wanted the question to accept input, and output a value based on that.  However, in these instances, the code often just returned a static value, no matter the circumstances.  Similarly, there were some bugs (such as improper ASCII value for '?') which prevented effective testing/implementation.

Was the requirements complete? Explain
======================================

If this refers to whole testing of available code, I would say that the requirements were mostly complete.  Except for perhaps utilizing teach for adding answers (personal choice as well), there were no features I could see which weren't covered.

Bugs
====

**ISSUE Number: 1**

**BRIEF: Wrong ASCII character for "?"**

**Steps to reproduce: ask anything**

**Comments:**

**Time Spent: 5 Minutes**


**ISSUE Number: 2**

**BRIEF: Question for feet to miles says "feed" not "feet", does not append miles to return value**

**Steps to reproduce: ask('What is ____ feet in miles')**

**Comments: Adding miles to the return will fix any error**

**Time Spent: 2 Minutes**


**ISSUE Number: 3**

**BRIEF: Seconds since question does not calculate any legitimate value, no matter given date/time configuration**

**Steps to reproduce: ask('How many seconds since April')**

**Comments:**

**Time Spent: 5 Minutes**


**ISSUE Number: 4**

**BRIEF: Who created Python question returns BDFL as written out string (Benevolent Dictator For Life) rather than just BDFL**

**Steps to reproduce: ask('Who invented Python')**

**Comments:**

**Time Spent: 2 Minutes**


**ISSUE Number: 5**

**BRIEF: Too many arguments given**

**Steps to reproduce: See lines 56 and 57**

**Comments: Unsure of why this error is throwing, requirements don't specify**

**Time Spent: 5 Minutes**

Why are requirements tracing so important?
==========================================

It allows for easier correspondence between requirements and tests, helping with referencing and such.  Also prevents requirements from being missed.

How long did it take to complete this lab?
==========================================

I wasn't keeping close track, but I would say that the lab took me about 6-8 hours.