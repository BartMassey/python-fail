# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

# The += operator on lists appends the a copy of the
# right-hand operand to the left-hand operand. This
# makes z += y different from z = z + y.

# First, note that the append operator makes a (shallow)
# copy of both lists.
x = [[1]]
y = [[2]]
z = x + y
print(z)   # Prints [[1], [2]]
x[0][0] = 3
y[0][0] = 4
print(z)   # Prints [[3], [4]]
x[0] = 3
y[0] = 4
print(z)   # Prints [[3], [4]]

print()

# Now, note that append assignment operator makes a copy of
# just the right list.
x = [1]
z = x
y = [2]
z += y
print(z)   # Prints [1, 2]
x[0] = 3
print(z)   # Prints [3, 2]
y[0] = 3
print(z)   # Prints [3, 2]

print()

# The identity z = z + y === z += y does not hold.
x = [1]
z = x
y = [2]
z = z + y
print(z)   # Prints [1, 2]
x[0] = 3
print(z)   # Prints [1, 2]
y[0] = 3
print(z)   # Prints [1, 2]
