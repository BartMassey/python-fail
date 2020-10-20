# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

def check(n, x, y):
    if x != y:
        print("failed check", n)

# Replicating a list with * operator replicates
# the values. Combining this with the fact that
# lists are lvalues leads to a rich source of errors.

# Normal case.
check(1, [None] * 3, [None, None, None])

# Variables work fine.
x = None
check(2, [x] * 3, [None, None, None])

# Replication conjugates.
x = None
y = [x] * 3
check(3, y * 3, [
    None, None, None,
    None, None, None,
    None, None, None,
])

# Nesting nests.
x = [None]
y = [x] * 3
check(4, y * 3, [
    [None], [None], [None],
    [None], [None], [None],
    [None], [None], [None],
])

# But structure is shared: all elements point to the same
# cell.
x[0] = 1
check(5, y, [[1], [1], [1]])

# Here all elements in each column point to the same cell.
z = [[None]*3]*3
check(6, z, [
    [None, None, None],
    [None, None, None],
    [None, None, None],
])
z[0][0] = 1
check(7, z, [
    [1, None, None],
    [1, None, None],
    [1, None, None],
])

# Explicit list multiplication.
def listmult(n, l):
    return [e for _ in range(n) for e in l]

# Structure check.
x = [None]
y = [x] * 3
check(8, y, [[None], [None], [None]])

# Aliasing happens here also.
x[0] = 1
check(9, y, [[1], [1], [1]])
