# Python List Append Fail
Copyright © 2014 Bart Massey

In C, the statements `z = z + y` and `z += y` are
operationally equivalent. Because the C arithmetic and
boolean operators only operate on scalar types, this
identity is easy to enforce.

In Python `+` is overloaded as a binary list append
operator. The semantics of the operator are non-destructive:
a shallow copy of the operands is appended to get the
result. The other obvious choice would have been to
destructively append (force the tail of the left argument to
be the head of the right argument); this would have the
advantage of being constant time, but would be more
error-prone as other references to the left argument would
see the modification. A third choice would be to
semi-destructively append: modify the left argument to point
to a shallow copy of the right argument. It's not obvious
why this would be a good choice: it is neither efficient nor
safe.

In Python, as in C, there is a `+=` operator that applies
the binary operator implied by the name to the left-hand and
right-hand arguments and assigns the result to the left-hand
argument&mdash;or so one might infer. In actuality, the
assignment version of the operator semi-destructively
appends.

The same behavior is true for the other operators that apply
to lists and have assignment versions including `*`, and for
operators on sets such as `|` that have assignment versions.

This is a difficult behavior to change compatibly, since
presumably existing programs depend on both the binary and
assignment operator behaviors. In addition to the symbolic
operators, Python sets also have methods like `union()` that
are nondestructive of their arguments. Oddly, there seems to
be no standard nondestructive append() method for list:
perhaps because that name is already taken by the
semi-destructive functionality.

-----

This work is licensed under the "MIT License".  Please see
the file COPYING in the source distribution of this software
for license terms.
