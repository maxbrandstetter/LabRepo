Lab 2 Write-Up Max Brandstetter
-------------------------------

Explain the major differences between TDD and BDD
=================================================

At the simplest level, TDD and BDD differ in their focus, as TDD is concerned with the implementation of the program through testing while BDD is, as the name implies, primarily concerned with how the program will behave.  Beyond that, I would say that BDD allows for a clearer understanding between several parties, due to the familiar language used therein, while TDD is more focused toward the specific developer.  When tests are developed by a single individual, they are often the only ones who can extensively understand the purpose of the test.  This isn't to say that one is ultimately better, as it is dependent on use; BDD works well in creating specifications and coding to those specifications, while TDD is effective in creating several testable instances.  These instances may be less efficient and robuts than well used BDD, but there is definitely still worth in its use.

What is a mixin, what challenges can occur when testing them?  What order are they initialized in?
==================================================================================================

A mixin is a special kind of multiple inheritance in which we can combine multiple classes into one.  From what I understand, the challenges would lie in the multi-functionality that it offers.  If not used with care, mixins can carry over properties from its inheriting classes that may be unwanted, resulting in unexpected results.  As such, I would say that mixins introduce a need for awareness; rather than focusing purely on the functions that are intended to be used through that inheritance, the associations between properties and functions must also be looked at.  The concept of mixins is a bit confusing to me, so my best guess in regards to initialization would be that the instance of the mixin is initialized first, followed by the inherited members that make up the mixin.  

In python, what does "super" do?
================================

Super allows us to make add variations to inherited functions, while maintaining the same functionality.  Essentially, super helps us travel up the inheritance tree.  Through proper use, cleaner OO models can be made due to how it references parent functionality.

Were there any job stories that did not meet the criteria we discussed in class?  How did you handle this case?
===============================================================================================================

From what I could tell through working through the lab and rereading the job stories, none of them went blatantly outside of the criteria we discussed.  However, due to the nature of the assignment, the results expected from some of the tests were ambiguous and relied on our implementation, however simple or complex that may be.  In these cases, I generally consider the scenarios briefly, implemented them, then reworked them if I found my initial plans to be inefficient or otherwise faulty.  This was more common in the BDD portion, but similarly, I just assumed the return of some variable, as that could be switched to a check of program output (print) or removed entirely with few repercussions.

Which model did you find most challenging?  Why?
================================================

I definitely found the behavior driven model more challenging due to the obscurity of programming, I suppose.  Although it is meant to be most similar to common speech, using Behave and translating that to both python implementation, as well as implementation with necessary classes, made the task overwhelming.

Which model did you find easiest to update/maintain?
====================================================

Perhaps it's just inexperience, but I thought the test driven model was the easiest to update and maintain.  Each test only required a bit of reworking to function properly, after which it wasn't difficult to commit the changes for revision.

How did you test that logging occurred only when desired?
=========================================================

I feel that I skipped over logging more than I should have, so I didn't really utilize it that much.  In a couple cases during the BDD portion, I used logging to output an error message if reading/writing of a file was unsuccessful, so checking that that was done successfully was just a matter of implementing an if else statement.  
