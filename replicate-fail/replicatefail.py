# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

# Replicating a list with * operator replicates
# the values. Combining this with the fact that
# lists are lvalues leads to a rich source of errors.

print([None] * 3)

x = None
print([x] * 3)

x = None
y = [x] * 3
print(y)

x = [None]
y = [x] * 3
print(y)

x[0] = 1
print(y)

z = [[None]*3]*3
print(z)
z[0][0] = 1
print(z)
