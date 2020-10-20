# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

def check(n, x, y):
    if x != y:
        print("failed check " + str(n))

# For some reason, nil [] is an lvalue. 
# This can be really confusing.

# Two distinct lists, each handled separately.
x = []
y = []
x += [1]
y += [2]
check("1.1", x, [1])
check("1.2", y, [2])

# Now `x` and `y` effectively point at the same list.
x = []
y = x
x += [1]
y += [2]
check("2.1", x, [1, 2])
check("2.2", y, [1, 2])
