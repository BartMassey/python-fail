# Python Replicate Fail
Copyright © 2014 Bart Massey

Python's list-integer multiplication operator produces a
list consisting of the elements of a list repeated the
specified number of times, like `replicate` in Haskell.

Given a list `l` and an integer `n`

    l * n == n * l == [e for _ in range(n) for e in l]

This seems great although pretty error-prone, as accidental
multiplications of integers and lists are probably as common
as intentional ones and will produce no immediate error.

One bad consequence of Python's by-reference model, though,
is that the expressions produced by `*` end up sharing
storage. See the code for details.

-----

This work is licensed under the "MIT License".  Please see
the file COPYING in the source distribution of this software
for license terms.
