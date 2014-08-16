# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

# For some reason, nil [] is an lvalue. 
# This can be really confusing.

x = []
y = []
x += [1]
y += [2]
print(x, y)

x = []
y = x
x += [1]
y += [2]
print(x, y)
