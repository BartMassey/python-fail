# Python Module Import Fail
Copyright © 2014 Bart Massey

Names can be imported from Python modules for unqualified
use. One can also import the module itself, and use its
names qualified. Ideally, both kinds of import would end up
referring to the same symbol.

In Python, not so much. When you import a non-function
variable from a module, it is allowed, but gives a fresh
local copy of the variable. Now you have two.

Also, in Python a function with the same name as its module
is a problematic entity because of the syntactic ambiguity
of `.` as module qualifier and also a function attribute
specifier.

-----

This work is licensed under the "MIT License".  Please see
the file COPYING in the source distribution of this software
for license terms.
