# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

# The += operator on lists appends the a copy of the
# right-hand operand to the left-hand operand. This
# makes z += y different from z = z + y

x = [1]
y = [2]
z = x + y
print(z)
x[0] = 3
print(z)
y[0] = 3
print(z)

print()

x = [1]
z = x
y = [2]
z += y
print(z)
x[0] = 3
print(z)
y[0] = 3
print(z)

print()

x = [1]
z = x
y = [2]
z = z + y
print(z)
x[0] = 3
print(z)
y[0] = 3
print(z)
