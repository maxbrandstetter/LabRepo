"""
This is a test of doctests, didn't work as I had hoped
Unsure of how to incorporate doctests properly
"""

def add_numbers(x, y):
    """
    Return the sum of the two given numbers

    >>> x = 4
    >>> y = 6
    >>> print x + y
    10

    .. testsetup:: *

        x = 5
        y = 10

    .. testcode:: addition

        print x + y

    .. testoutput:: addition

        15

    """
    return x + y
