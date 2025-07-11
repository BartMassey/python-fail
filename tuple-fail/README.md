# Python Tuple/List Inequality Fail
Copyright © 2025 Bart Massey

In Python a tuple is treated as not-equal to a list with the
same elements. Python requires converting lists to tuples to
make a set of lists, which makes this pretty bug-prone.

A list and a tuple with the same elements should be treated
as equal, since a tuple is just a "frozen" list. Note that
this is the case with for example `set` and `frozenset`,
which makes the situation more frustrating.

-----

This work is licensed under the "MIT License".  Please see
the file COPYING in the source distribution of this software
for license terms.
