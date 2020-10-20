# Python Fail
Copyright © 2014 Bart Massey

This repo documents some of the failings of the Python
programming language that I have discovered as I have taught
it in introductory programming classes. These problems are
significant both for beginning programmers and for software
engineers. In each case, I have tried to suggest solutions
that could be incorporated in a PEP to ameliorate the
problem.

I have quite a bit of experience with programming language
design and implementation, but I am in no way a Python
guru. I would be grateful for corrections, suggestions and
constructive critique.

In no particular order:

* append-fail: The choice of `+=` as an append operator causes confusion.
* expr-fail: Implicit conversions between boolean and
  integer values combine badly with odd precedence rules. 
* module-fail: Module variable scope rules are confusing, and
  the existence of function attributes makes them worse.
* nil-fail: The empty list is an lvalue, with odd consequences.
* replicate-fail: The list multiply operator doesn't copy
  (or even shallow copy) its prototype, inhibiting 2D array creation.
* scope-fail: Adding an assignment to a Python program can
  change the scoping of its variables in surprising ways.

This work is licensed under the "MIT License".  Please see
the file COPYING in the source distribution of this software
for license terms.
