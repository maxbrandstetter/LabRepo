Lab 1 Write-Up Max Brandstetter
-------------------------------

What was the hardest part of this lab?
======================================

Personally, I felt that the majority of the lab was straightforward.  However, since I was unable to make it to the lab on Saturday, I spent time throughout looking up information regarding proper usage and still feel as if some components of my lab are incorrect or improperly done.  Anyway, I would say that as such, the hardest part of the lab was actually setting up Drone.IO properly, which I'm pretty sure I still haven't done.  I encountered issues with default build parameters and ended up just using the default, meaning that despite my efforts, I haven't been able to have Drone.IO build my doctests.

During the course of this lab, why did we exclude .pyc files?
=============================================================

We excluded .pyc files because those merely contain byte code for their corresponding source code.  This allows us to run the source code without needing an explicit .exe, but offers no benefit to us directly.  Basically, since we won't be directly using or editing the .pyc files, and they are mostly used in compilers, it proves unnecessary to include.

Name three files which would likely need to have a gitignore added?
===================================================================

We may want to include installer logs such as pip-log.txt in our gitignore, although I suppose that's a bit circumstantial.  Other files that might be good to include would be those such as .cache files, .bat files, and .exe files.

What is a pyunit TestCase?
==========================

PyUnit merely offers test formats through python, thus specifying those test cases.  The test case itself is a set of conditions set up by the tester to ensure that certain features are functioning properly.  

What is the difference between a git cherry pick and a rebase?
==============================================================

Git rebase seems to be more reminiscent of a full merge, as it will move a set of changes or commits to the master branch from some other branch.  Git cherry pick, on the other hand, although capable of selecting numerous commits is more focused.  Furthermore, it does not move the entirety of the branch, but merely copies those specific commits to the location specified.

How could you use git to print out just the author name of a given file for the current version of the repo?
============================================================================================================

I would say that the following is the simplest way to print the author name:

.. code::
    git shortlog -sn

This will generate a list of authors for the present repository, but excludes other unnecessary information.

During this lab did you explore Tortoise Git or GIT Extensions? If not take a look at them, they probably would be useful for the remainder of the class
========================================================================================================================================================

I did not look into either very extensively over the course of the lab.  However, I did look at the functionality that they provide as a result of this question and may try to utilize them in the future.

Did you find the second issue in get_triangle_type? Did you choose to test the code as is or fix the code in get_triangle_type
===============================================================================================================================

I believe I found the second issue, that being that under the the if statement handling a as a tuple, b is assigned to b[1] instead of a[1].  As such, I fixed the code in get_triangle_type and tested based on that fixed version.