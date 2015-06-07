Lab 8 Writeup
-------------

**How was this test useful?**

The test allowed me to see what errors could potentially occur during importing of classes, functions, and methods.  Running this program after making changes to a repository, for example, would help me find those errors that resulted from imports more quickly.  I suppose overall it offers shorter times in debugging.

**How did you report errors found by this test? How difficult would it be for a developer to debug these errors?**

I used logging to output the errors.  For classes, modules, and functions, I had virtually the same format.  The program would display the class/module/function that was being imported, the exception that was raised, and what the exception message was.  For modules and classes, I added a tidbit on where it was being imported from in order to further narrow it down.  By adding detail such as this, developers can easily come in and if an error occurs, pinpoint it and fix it with relative ease.

**What other things would be useful to have in a sanity test?**

It would benefit any UI testing for sure, although in this instance, it might help to add property calls, checking initial values, and other similar values.

**How would you sanity test a UI? A database interface? A webpage? A C# program?**

For a UI, I might press some series of known inputs and ensure that the page/visuals I expect to display actually display correctly.

For a database interface, I would test reads/writes to some test database, as well as connections/disconnections to some test database.

For a webpage, I would sanity test by pressing buttons, clicking links, and entering inputs where I could, ensuring that any results were expected.

For a C# program, I suppose I would sanity test similarly to what we did here; I would test importing of namespace, class instantiations, as well as function or method calls.