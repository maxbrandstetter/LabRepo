What was the hardest part of this lab?
======================================
Honestly, figuring out an effective way to output the performance testing was probably the most difficult part.  Thinking of decent additions proved challenging, mostly because I lack creativity, but it wasn't difficult per se.

What is the difference between performance testing and performance measurement?
===============================================================================
Performance testing ensures that the standard for performance, whatever that may be, is met by the program.  Performance measurement, on the other hand, is an output of those performance values (a numerical or similar representation of performance).

What new bugs did you encounter with the new code?
==================================================
Finding the 1000th Fibonacci number seemed inconsistent.
Sometimes, my own requirements for performance and those set by you were not met by either my system, or drone.io.

Did you mock anything to speed up performance testing? Do you see any issues with this?
=======================================================================================
I did not mock anything to speed up performance testing.  However, I could see where it could be useful.  For instance, in the generation of characters for writing, I merely used the string library through python.  Mocking could be used instead to select specific characters, so no, I see no issue with using mock to speed up performance testing.  

Generate at least 5 performance measurement value sets and graphs (these sets must be worthwhile)
=================================================================================================
I used matplotlib to the best of my ability, output was saved to a graphs folder.

Explain Load Testing, stress testing, endurance testing, spike testing configuration testing and isolation testing. How did you implement each of these?
=========================================================================================================================================================
Load testing involves putting an interface under a constant and often consistent load.  Stress testing is used to test the capacity of the interface to handle specific loads.  Endurance testing is used to ensure that an interface can sustain a continuous expected load.  Spike testing involves causing sudden increases in the current load to examine how well the interface handles it.  Configuration testing involves changing system or environmental settings to ensure that the interface behaves the same regardless of irrelevant conditions.  Isolation testing involves repeating a problem test in order to find where the issue lies.
Load Testing (Stress/Endurance too?): I compared processing time when different numbers of questions had been asked.  A poor description, but as the number of questions increases, the response and store time of text questions increases (load increases, time increases).  I also testing writing/reading a value far exceeding what the requirements expected and noted the output.
Isolation Testing: Done with almost all other tests, from what I understand.

How long did this lab take to accomplish?
=========================================
6-8 Hours, given my difficulties with output, as well as wait time for tests